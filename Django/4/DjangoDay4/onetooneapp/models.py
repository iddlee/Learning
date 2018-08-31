from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

class Card(models.Model):
    cardno = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    per = models.OneToOneField(Person,on_delete=models.CASCADE)  # 负责维护“一对一”关系


