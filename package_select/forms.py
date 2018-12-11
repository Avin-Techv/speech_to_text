from django import forms
from .models import Sound


class SelectPackageForm(forms.ModelForm):

    class Meta:
            model = Sound
            fields = []


class UploadFileForm(forms.ModelForm):

    class Meta:
            model = Sound
            fields = ['document']


class RecordFileForm(forms.ModelForm):

    class Meta:
            model = Sound
            fields = []
