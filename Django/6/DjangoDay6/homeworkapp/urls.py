from django.urls import path
from homeworkapp.views import *

urlpatterns = [
    path('goreg/',go_reg),
    path('check/<regname>/',checkRegName),

]