from django.urls import path
from homeworkapp.views import *

app_name = "homeworkapp"

urlpatterns = [
    path('go/',go_student),
    path('showall/',getallstudents,name="all"),
]