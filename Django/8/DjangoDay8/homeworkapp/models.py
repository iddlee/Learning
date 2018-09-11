from django.db import models

class Classes(models.Model):
    name = models.CharField(max_length=10)

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    cls = models.ForeignKey(Classes,on_delete=models.CASCADE)


