from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import DocumentForm


class UserHome(View):
    template_name = 'home.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'package_select/home.html', {
        'form': form
    })
