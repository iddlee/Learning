from django.db import models

# 学校模型
class School(models.Model):
    schname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.schname

# 学生模型
class Student(models.Model):
    stuname = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    score =models.FloatField()
    stuschool = models.ForeignKey(School,on_delete=models.CASCADE)  # 使用该属性维护“一对多”的关系

    def __str__(self):
        return self.stuname
