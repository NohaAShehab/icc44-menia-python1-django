from django.db import models

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(null=True, blank=True)
    image= models.ImageField(upload_to='tracks/images/', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"