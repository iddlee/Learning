from django.urls import path
from myapp.views import *

urlpatterns = [
    path('welcome/',hello),
    path('allbooks/',show_books),
    path('reg/',show_reg),
    path('regaction/',reg_action),
]