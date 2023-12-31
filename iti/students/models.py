from django.db import models
from django.shortcuts import  reverse

from tracks.models import Track
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,null=True, unique=True)
    image = models.ImageField(upload_to='students/images/', max_length=200, null=True)
    # image save only the image
    grade=  models.IntegerField(default=100, null=True)
    gender = models.CharField(
        choices=[('m', 'Male'), ('f', 'Female')])
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True
                              ,related_name='students')
    # track ==> represent track object in db
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"


    # def get_image_url(self):
    #     return f'/static/students/images/{self.image}'

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        url = reverse('students.show', args=[self.id])
        return url

    def get_delete_url(self):
        url = reverse('students.delete', args=[self.id])
        return url