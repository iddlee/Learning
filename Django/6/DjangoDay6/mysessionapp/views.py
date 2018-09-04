from django.http import HttpResponse
from django.shortcuts import render

def add_session_value(request):
    request.session["color"] = "yellow"  # 设置session的color属性
    print("该sessionid为：",request.session.session_key)
    return render(request,'session.html')


def modify_session_value(request):
    request.session["color"] = "green"  # 设置session的color属性
    request.session["country"] = "China"
    print("该sessionid为：", request.session.session_key)
    return render(request, 'session.html')

def addCookie(request):
    response = HttpResponse("已经成功添加Cookie")
    response.set_cookie("ice","Ice-Cream",30)   # 设置Cookie
    response.set_cookie("hero", "Man", 30)
    response.set_cookie("beautiful", "Girl")
    return response


def show_cookies(request):
    return render(request,'mycookie.html')

