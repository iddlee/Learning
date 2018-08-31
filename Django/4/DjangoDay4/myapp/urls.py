from django.urls import path
from myapp.views import *

urlpatterns = [
    path('go/',go_country),
    path('add/',add_country),
    path('showall/',show_all),
    path('delete/<int:country_id>/',delete_byid),
]