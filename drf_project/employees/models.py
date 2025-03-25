from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=10)
    ename = models.CharField(max_length=30)
    desg = models.CharField(max_length=15)

    def __str__(self):
        return self.ename