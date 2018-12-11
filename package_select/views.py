from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import SelectPackageForm, UploadFileForm, RecordFileForm
from .models import Document

from django.views.generic import View
from django.urls import reverse_lazy


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



