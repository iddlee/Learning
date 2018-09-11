from django.http import HttpResponseRedirect
from django.shortcuts import render
from homeworkapp.models import *


# 进入添加班级页面
def goclass(request):
    return render(request, 'addclass.html')


# 进入添加学生页面
def gostudent(request):
    classes = Classes.objects.all()
    return render(request, 'addstudent.html', locals())


# 添加班级
def add_class(request):
    class_name = request.POST["class_name"]
    Classes.objects.create(name=class_name)
    msg = class_name + "添加成功"
    return render(request, 'addclass.html', {"msg": msg})


# 添加学生
def add_student(request):
    stu_name = request.POST["stu_name"]
    stu_age = request.POST["stu_age"]
    stu_sex = request.POST["stu_sex"]
    stu_class_id = request.POST["stu_class"]  # 获取学生所在的班级id
    Student.objects.create(name=stu_name, age=stu_age, sex=stu_sex, cls_id=stu_class_id)
    return HttpResponseRedirect("/homeworkapp/showall/")


# 查询所有学生
def show_allstudents(request):
    students = Student.objects.all()
    return render(request, 'students.html', locals())
