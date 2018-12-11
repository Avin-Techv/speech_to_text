from django.urls import path
from .views import SelectPackage, UploadFile, RecordFile, FilesList
app_name = 'package_select'

urlpatterns = [
    path('', SelectPackage.as_view(), name="home"),
    path('upload/', UploadFile.as_view(), name="upload"),
    path('record/', RecordFile.as_view(), name="record"),
    path('files/', FilesList.as_view(), name="files")
]
