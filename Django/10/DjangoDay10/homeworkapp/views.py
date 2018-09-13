from django.http import HttpResponseRedirect
from django.shortcuts import render
from homeworkapp.models import User
from homeworkapp.forms import UserForm

def register(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)  # 接收表单的POST提交数据
        if userForm.is_valid():
            name = userForm.cleaned_data["name"]
            password = userForm.cleaned_data["password"]
            repassword = userForm.cleaned_data["repassword"]
            email = userForm.cleaned_data["email"]
            qq = userForm.cleaned_data["qq"]
            if password != repassword:
                print("密码不一致！")
                return HttpResponseRedirect("/homeworkapp/reg/")
            print("所有验证都通过~~~~~~~")
            User.objects.create(username=name,password=password,email=email,qq=qq) # 注册，插入数据库
            return render(request,'success.html')
        else:
            return HttpResponseRedirect("/homeworkapp/reg/")
    else:
        userForm = UserForm()
        return render(request,'register.html',{'regform':userForm})
