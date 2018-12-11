from django import forms
from .models import Document


class SelectPackageForm(forms.ModelForm):

    class Meta:
            model = Document
            fields = []


class UploadFileForm(forms.ModelForm):

    class Meta:
            model = Document
            fields = ['document']


class RecordFileForm(forms.ModelForm):

    class Meta:
            model = Document
            fields = []
