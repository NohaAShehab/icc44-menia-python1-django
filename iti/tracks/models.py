from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(null=True, blank=True)
    image= models.ImageField(upload_to='tracks/images/', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def get_index_url(cls):
        return reverse('tracks.index')


    @classmethod
    def get_specific_object(cls, id):
        return cls.objects.get(id=id)


    def get_image_url(self):
        return  f'/media/{self.image}'


    def get_edit_url(self):
        return  reverse('tracks.edit', args=[self.id])