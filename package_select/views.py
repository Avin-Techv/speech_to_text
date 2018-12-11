from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import SelectPackageForm, UploadFileForm, RecordFileForm


class SelectPackage(FormView):
    template_name = "package_select/home.html"
    form_class = SelectPackageForm
    success_url = '.'


class UploadFile(FormView):
    template_name = "package_select/upload_file.html"
    form_class = UploadFileForm
    success_url = '.'


class RecordFile(FormView):
    template_name = "package_select/record_file.html"
    form_class = RecordFileForm
    success_url = '.'
