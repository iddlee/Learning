from django.urls import path
from reverseurlapp.views import *

# 使用URL反向解析，必须在应用路由模块中添加app_name变量，变量值为当前应用名称
app_name = 'reverseurlapp'

urlpatterns = [
    path('all/',show_books),
    path('detail/<bid>/',detail_book,name="detail"),
    path('update/',update_book,name="bookupdate"),
]