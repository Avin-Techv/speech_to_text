import os

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, FormView, TemplateView
from .forms import SelectPackageForm, UploadFileForm, RecordFileForm
from .models import Document

from django.http import HttpResponse
import speech_recognition as sr
from pydub import AudioSegment

from os import path


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
        file_id = request.POST.get('file_id')
        file_object = Document.objects.get(id=file_id)
        sound = AudioSegment.from_mp3(file_object.document)
        AUDIO_FILE = os.path.join(settings.MEDIA_ROOT, "transcript.wav")
        sound.export(AUDIO_FILE, format="wav")


        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

            print("Transcription: " + r.recognize_google(audio))
