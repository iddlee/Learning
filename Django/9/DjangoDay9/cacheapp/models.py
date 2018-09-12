from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "蛋糕"
        verbose_name_plural = "蛋糕"
