from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=15)

    def __str__(self):
        return self.name