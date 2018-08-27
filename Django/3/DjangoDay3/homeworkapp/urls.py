from django.urls import path
from homeworkapp.views import *

urlpatterns = [
    path('fruits/',show_fruits),
    path('goreg/',go_reg),
    path('reg/',reg),
    path('<tag>/',sports),
]