from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    king = models.CharField(max_length=10)
