from django.urls import path
from pageapp.views import get_students

app_name = 'pageapp'

urlpatterns = [
    path('students/<int:page_param>/',get_students,name="students"),
]