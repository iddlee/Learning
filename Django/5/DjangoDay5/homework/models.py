from django.db import models


class Husband(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()


class Wife(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    husband = models.OneToOneField(Husband, on_delete=models.CASCADE)


class Country(models.Model):
    couname = models.CharField(max_length=20)


class Province(models.Model):
    proname = models.CharField(max_length=20)
    cou = models.ForeignKey(Country, on_delete=models.CASCADE)
