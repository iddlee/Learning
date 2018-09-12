from django.urls import path
from formapp.views import *

app_name = "formapp"

urlpatterns = [
    path('milk/',milk_form,name='milk'),
]