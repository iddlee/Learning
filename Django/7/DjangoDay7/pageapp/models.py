from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    score = models.FloatField()

    def __str__(self):
        return self.name
