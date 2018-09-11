from django.urls import path
from homeworkapp.views import *

app_name = "homeworkapp"

urlpatterns = [
    path('goclass/',goclass),
    path('showall/',show_allstudents),
    path('gostudent/',gostudent,name="gostu"),
    path('addclass/',add_class,name="addclass"),
    path('addstu/',add_student,name="addstudent"),
]