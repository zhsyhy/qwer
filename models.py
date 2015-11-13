qefrom django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Study = models.CharField(max_length=30)
    Labroom = models.CharField(max_length=100)
    Workroom = models.CharField(max_length=100)
    Achievement = models.CharField(max_length=500)
    Date = models.CharField(max_length=100)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Leixing = models.CharField(max_length=30)
class order(models.Model):
    orderusername = models.CharField(max_length=30)
    daoshi = models.CharField(max_length=30)
    xingming = models.CharField(max_length=30)
    orderdata = models.CharField(max_length=30)
    telephone = models.CharField(max_length=100)
    yes = models.CharField(max_length=30)

