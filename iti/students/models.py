from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,null=True, unique=True)
    image = models.CharField(max_length=200, null=True)
    grade=  models.IntegerField(default=100, null=True)
    gender = models.CharField(
        choices=[('m', 'Male'), ('f', 'female')])
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
