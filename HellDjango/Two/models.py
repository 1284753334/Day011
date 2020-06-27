from django.db import models

# Create your models here.
class Student (models.Model):

    s_nama = models.CharField(max_length=20)
    s_age = models.IntegerField(default=1)

