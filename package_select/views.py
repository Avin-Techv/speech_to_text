import os
import time
import schedule

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, FormView, TemplateView
from .forms import SelectPackageForm, UploadFileForm, RecordFileForm
from .models import Document

from django.http import HttpResponse, JsonResponse
from pydub import AudioSegment

from os import path

import speech_recognition as sr
from gtts import gTTS
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer

mixer.init()


class SelectPackage(FormView):
    template_name = "package_select/home.html"
    form_class = SelectPackageForm
    success_url = '.'


class UploadFile(FormView):
    template_name = "package_select/upload_file.html"
    form_class = UploadFileForm
    success_url = '.'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class RecordFile(FormView):
    template_name = "package_select/record_file.html"
    form_class = RecordFileForm
    success_url = '.'


class FilesList(TemplateView):
    template_name = "package_select/files.html"

    def get(self, request, *args, **kwargs):
        documents = Document.objects.all()
        return render(request, 'package_select/files.html', {'documents': documents})


class AnalyseFile(View):
    def post(self, request, *args, **kwargs):
        try:
            file_id = request.POST.get('file_id')
            file_object = Document.objects.get(id=file_id)
            audio_file = os.path.join(settings.MEDIA_ROOT, str(file_object.document))
            sound = AudioSegment.from_mp3(audio_file)
            sound.export(audio_file, format="wav")

            recogniser = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio = recogniser.record(source)  # read the entire audio file

                content = recogniser.recognize_google(audio)
            return render(request, 'package_select/files.html', {'content': content})
        except IOError:
            pass


class RecordPackageFile(TemplateView):
    template_name = "package_select/record_file_package.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs


class TranscribeAudio(View):
    def get(self, request, *args, **kwargs):
        try:
            # obtain audio from the microphone
            isRecording = request.GET.get('isRecording', '')
            while isRecording:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # print("Please wait. Calibrating microphone...")
                    # listen for 1 second and create the ambient noise energy level
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Recording Started... Say Something...")
                    # audio = r.listen(source, phrase_time_limit=5)
                    # transcribed_text = r.recognize_google(audio)
                    transcribed_text = r.recognize_google(r.listen(source))
                    if transcribed_text != None:
                        print("I think you said '" + transcribed_text + "'")
                        tts = gTTS(text="I think you said " + transcribed_text, lang='en')
                        tts.save("response.mp3")
                        mixer.music.load('response.mp3')
                        mixer.music.play()
                        return JsonResponse({'transcribed_text': transcribed_text}, status=200)
                    else:
                        pass

        except sr.UnknownValueError:
            error = "Google Speech Recognition could not understand audio"
            return render(request, 'package_select/record_file_package.html', {'error': error})
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
