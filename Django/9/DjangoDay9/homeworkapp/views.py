from django.core.cache import cache
from django.shortcuts import render
from homeworkapp.models import Student

def go_student(request):
    return render(request,'students.html')

def getallstudents(request):
    value = cache.get("all")  # 尝试从缓存中获取所有学生信息
    if value:
        return render(request,'students.html',{"students":value,"msg":'恭喜，缓存命中了！'})
    else:
        students = Student.objects.all()  # 从数据库中查询
        cache.set("all",students,60)   #  存入缓存，并设置缓存时间
        return render(request,'students.html',{"students":students,"msg":'从MySQL数据库中查询...'})
