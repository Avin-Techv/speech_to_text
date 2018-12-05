from django import forms
from .models import Sound


class SelectPackageForm(forms.ModelForm):

    class Meta:
            model = Sound
            fields = ['input_method', 'document', 'recognition_package']
