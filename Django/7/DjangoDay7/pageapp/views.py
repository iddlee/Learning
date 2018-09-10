from django.core.paginator import Paginator
from django.shortcuts import render
from pageapp.models import Student

def get_students(request,page_param=1):
    students = Student.objects.all() # 查询所有的学生
    paginator = Paginator(students,3) # 创建分页器对象，第一个参数是记录的容器，第二个参数每页显示的记录数
    page = paginator.page(page_param)  # 获取指定页码的数据，以返回的Page对象封装这些数据
    return render(request,'students.html',{'paginator':paginator,'page':page})
