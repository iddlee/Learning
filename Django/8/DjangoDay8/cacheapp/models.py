from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.FloatField()
