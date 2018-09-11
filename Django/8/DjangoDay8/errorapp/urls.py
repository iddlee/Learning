from django.urls import path,include
from errorapp.views import *


urlpatterns = [
    path('compute/',compute),
    path('gowrong/',go_wrong),
]