from django.http import HttpResponse
from django.shortcuts import render


def go_login(request):
    return render(request, 'session/login.html')


def go_success(request):
    return render(request, 'session/success.html')


def login(request):
    if request.method == 'POST':    # 判断是否为POST请求
        login_name = request.POST["loginname"]
        login_pwd = request.POST["loginpwd"]
        if login_name == "tom" and login_pwd == "123456":  # 判断用户名和密码是否正确
            request.session["logname"] = login_name  # 将登录用户名存储于session会话范围内
            return render(request, 'session/success.html')
        else:   # 信息输入错误
            return render(request, 'session/login.html', {"msg": "用户名或密码输入错误！"})
    else:
        return HttpResponse("非法的提交方式！")
