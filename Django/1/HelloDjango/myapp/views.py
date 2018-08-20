from django.http.request import QueryDict
from django.shortcuts import render,HttpResponse

def hello(request):
    return HttpResponse("<h3 style='color:red'>Hello,Django,Welcome to Django!</h3>")

def show_books(request):
    return render(request,'books.html')

def show_reg(request):
    return render(request,'reg/register.html')

def reg_action(request):
    print("注册的用户名是：",request.POST.get("regName"))
    print("注册的密码是：",request.POST.get("regPwd"))
    print("注册的QQ是：",request.POST.get("regQQ"))
    return render(request,'reg/success.html')

