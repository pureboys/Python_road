from django.db import models


# Create your models here.
class Info(models.Model):
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    status = models.CharField(max_length=32, default=False)


class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)




