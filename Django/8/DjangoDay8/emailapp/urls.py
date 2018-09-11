from django.urls import path
from emailapp.views import *

urlpatterns = [
    path('go/',go_email),
    path('getemail/<int:state_code>/',get_emails),
]