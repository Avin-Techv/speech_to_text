from django.urls import path
from .views import FileUpload
app_name = 'package_select'

urlpatterns = [
    path('', FileUpload.as_view(), name="home")
]
