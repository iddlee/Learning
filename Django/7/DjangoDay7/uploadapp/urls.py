from django.urls import path
from uploadapp.views import *

app_name = 'uploadapp'

urlpatterns = [
    path('goupload/',go_upload),
    path('upload/',upload,name="uploadfile"),
]