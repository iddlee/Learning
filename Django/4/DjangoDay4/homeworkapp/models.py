from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    salary = models.FloatField()
