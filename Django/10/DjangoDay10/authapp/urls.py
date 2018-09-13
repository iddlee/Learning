from django.urls import path
from authapp.views import *

app_name = "authapp"

urlpatterns = [
    path('goreg/',go_register),
    path('gologin/',go_login,name="gologin"),
    path('gosuccess/',go_success),
    path('govip/',go_vip),
    path('reg/',reg,name="reg"),
    path('login/',user_login,name="login"),
    path('logout/',log_out,name="logout"),
]