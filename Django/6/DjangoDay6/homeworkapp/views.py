from django.http import HttpResponse
from django.shortcuts import render
from homeworkapp.models import User

def go_reg(request):
    return render(request,'register.html')

def checkRegName(request,regname):
    user_queryset = User.objects.filter(username=regname)
    json = ""
    if user_queryset:
        json = "{\"info\":\"该用户名已存在，请选择其他用户名！\",\"isok\":\"sorry\"}"
        return HttpResponse(json)
    else:
        json = "{\"info\":\"恭喜，可以使用该用户名\",\"isok\":\"ok\"}"
        return HttpResponse(json)

