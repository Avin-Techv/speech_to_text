from django.urls import path
from .views import SelectPackage
app_name = 'package_select'

urlpatterns = [
    path('', SelectPackage.as_view(), name="home")
]
