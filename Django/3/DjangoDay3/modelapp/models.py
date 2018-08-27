from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    ticket = models.FloatField()
