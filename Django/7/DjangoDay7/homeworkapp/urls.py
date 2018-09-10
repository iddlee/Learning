from django.urls import path
from homeworkapp.views import *

app_name = "homeworkapp"

urlpatterns = [
    path('gologin/', gologin, name="gologin"),
    path('login/', login, name="login"),
    path('success/', gosuccess),

    path('goanimal/', goanimal),
    path('getimg/<animal>/', send_imgpath),
]
