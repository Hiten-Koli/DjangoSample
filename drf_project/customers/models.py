from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.CharField(max_length=10)
    cname = models.CharField(max_length=30)
    age = models.CharField(max_length=15)

    def __str__(self):
        return self.cname