from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

class Subject(models.Model):
    name = models.CharField(max_length=10)
    stu = models.ManyToManyField(Student,through="Relation")   # 指向中间模型

# 中间模型
class Relation(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)   # 创建外键，维护关系，必须添加
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)   # 创建外键，维护关系，必须添加
    score = models.FloatField()  # 额外添加的字段

