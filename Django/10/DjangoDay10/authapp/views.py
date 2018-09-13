from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from authapp.models import MyUserModel
from django.http import HttpResponseRedirect
from django.shortcuts import render

@login_required(login_url="/authapp/goreg/")
def go_vip(request):
    return render(request,'user_vip.html')

def go_register(request):
    return render(request,'user_register.html')

def go_login(request):
    return render(request,'user_login.html')

def go_success(request):
    login_name = request.GET.get('login_name',"")
    return render(request,'user_success.html',locals())

def reg(request):
    regname = request.POST["regname"]
    regpwd = request.POST["regpwd"]
    regtel = request.POST["regtel"]
    regqq = request.POST["regqq"]
    MyUserModel.objects.create_user(username=regname,password=regpwd,tel=regtel,qq=regqq)   # 添加到数据库中的auth_user表,create_user()对密码加密
    return HttpResponseRedirect("/authapp/gologin/")

def user_login(request):
    logname = request.POST["logname"]
    logpwd = request.POST["logpwd"]
    user = authenticate(username=logname,password=logpwd)  # 认证用户，判断用户名和密码是否正确
    print("logname=",logname,"logpwd",logpwd,"user=",user)
    if user:
        login(request,user)   # 将用户标识保存到session中
        return HttpResponseRedirect("/authapp/gosuccess/?login_name="+logname) # 重定向，并传递Get参数
    else:
        return render(request, 'user_login.html', {"msg": "用户名或密码错误，请重新登录！"})


def log_out(request):
    logout(request)   # 登出
    return HttpResponseRedirect("/authapp/gologin/")

