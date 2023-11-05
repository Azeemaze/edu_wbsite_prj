from django.db import models

# Create your models here.


class Registration(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Email = models.EmailField()
    Mobile = models.IntegerField()
    Country = models.CharField(max_length=150)
    State = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Hobbies = models.CharField(max_length=100)
    Upload_image = models.ImageField(upload_to="images")
