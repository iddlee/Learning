from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from homeworkapp.models import *


def gologin(request):
    return render(request, 'login.html')


def goanimal(request):
    return render(request, 'animal.html')


def gosuccess(request):
    return render(request, 'welcome.html')


def login(request):
    login_name = request.POST["login_name"]
    login_pwd = request.POST["login_pwd"]
    user_queryset = User.objects.filter(username=login_name, password=login_pwd)
    if user_queryset:   # 如果登录信息正确
        request.session["loginname"] = login_name   # 设置session中的属性值
        return HttpResponseRedirect("/homeworkapp/success/")
    else:
        return render(request, 'login.html', {'msg': '用户名或密码错误，请重新登录'})


def send_imgpath(request, animal):
    if animal == "dog":
        return JsonResponse({"imgpath": "/static/images/dog.jpg"})
    else:
        return JsonResponse({"imgpath": "/static/images/cat.jpg"})