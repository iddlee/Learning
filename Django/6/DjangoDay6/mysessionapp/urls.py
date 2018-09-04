from django.urls import path
from mysessionapp.views import *

urlpatterns = [
    path('addsession/',add_session_value),
    path('modsession/',modify_session_value),
    path('addcookie/',addCookie),
    path('showcookie/',show_cookies),
]