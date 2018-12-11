from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import SelectPackageForm, UploadFileForm, RecordFileForm


class SelectPackage(FormView):
    template_name = "home.html"
    form_class = SelectPackageForm
    success_url = '.'


class UploadFile(FormView):
    template_name = "upload_file.html"
    form_class = UploadFileForm
    success_url = '.'


class RecordFile(FormView):
    template_name = "record_file.html"
    form_class = RecordFileForm
    success_url = '.'

