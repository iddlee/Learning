from django.urls import path
from templateapp.views import *

urlpatterns = [
    path('xian/',go_xian),
    path('filter/',show_filter),
    path('locals/',use_locals)
]