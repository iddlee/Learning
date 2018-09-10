from django.db import models

# 出版社模型
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = "出版社"


# 作者模型
class Author(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"

# 书籍模型
class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)  # Publisher与Book是“一对多”的关系
    author = models.ManyToManyField(Author,through="ABRelation")  # Book与Author是"多对多"关系
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = "书籍"

# "多对多"关系的中间模型
class ABRelation(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "书-作者关系"
        verbose_name_plural = "书-作者关系"
