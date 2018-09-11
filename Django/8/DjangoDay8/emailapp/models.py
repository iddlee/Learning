from django.db import models

class Email(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    sender = models.CharField(max_length=10)
    state = models.IntegerField(default=0)  # 邮件状态，0未读，1已读
