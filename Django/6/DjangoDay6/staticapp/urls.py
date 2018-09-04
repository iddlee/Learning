from django.urls import path
from staticapp.views import *

urlpatterns = [
    path('go/',show),
]