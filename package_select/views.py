from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import SelectPackageForm


class SelectPackage(FormView):
    template_name = "home.html"
    form_class = SelectPackageForm
    success_url = '.'

