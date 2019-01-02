from django.urls import path
from .views import SelectPackage, UploadFile, RecordFile, FilesList, AnalyseFile, RecordPackageFile, TranscribeAudio
app_name = 'package_select'

urlpatterns = [
    path('', SelectPackage.as_view(), name="home"),
    path('upload/', UploadFile.as_view(), name="upload"),
    path('record/', RecordFile.as_view(), name="record"),
    path('record_package/', RecordPackageFile.as_view(), name="record_package"),
    path('transcribe_audio/', TranscribeAudio.as_view(), name="transcribe_audio"),
    path('files/', FilesList.as_view(), name="files"),
    path('analyse/', AnalyseFile.as_view(), name="analyse")
]
