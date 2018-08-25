from django.urls import path,re_path
from myapp.views import *

urlpatterns = [
    path('link/',go_link),
    path('gohobby/',show_hobby),
    path('book/<author>/<price>/',show_author),
    path('convert/<int:a>/<int:b>/',convert),
    re_path('hello/$',hello),
]