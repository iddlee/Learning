from django.urls import path,include
from cacheapp.views import *

urlpatterns = [
    path('cake/<cake_id>/',memcached_getdata),
]