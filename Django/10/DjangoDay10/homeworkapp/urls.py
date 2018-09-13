from django.urls import path
from homeworkapp.views import *

app_name = 'homeworkapp'

urlpatterns = [
    path('reg/',register,name="reg"),
]