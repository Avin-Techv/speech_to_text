from django import forms
from .models import Sound


class SelectPackageForm(forms.ModelForm):
    file_path = forms.CharField(max_length=50)

    class Meta:
            model = Sound
            fields = ['description', 'sound']
