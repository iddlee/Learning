from django.urls import path
from templateapp.views import *

urlpatterns = [
    path('mydict/',dict_info),
    path('obj/',object_info),
    path('list/',list_info),
    path('ifdemo/',iftag),
    path('fordemo/',fortag),
]