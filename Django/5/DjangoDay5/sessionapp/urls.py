from django.urls import path
from sessionapp.views import *

app_name = "sessionapp"

urlpatterns = [
    path('gologin/', go_login, name="gologin"),
    path('login/', login, name="userlogin"),
    path('success/', go_success),
]
