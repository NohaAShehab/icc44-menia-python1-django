from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"


    def get_image_url(self):
        return  f'/media/{self.image}'


    def get_edit_url(self):
        return  reverse('posts.edit',args=[self.id])

    def get_show_url(self):
        return  reverse('posts.show',args=[self.id])

    def get_delete_url(self):
        return  reverse('posts.delete',args=[self.id])

    @classmethod
    def get_all_objects(cls):
        # return cls.objects.filter(id__gt=1)
        return cls.objects.all()


    @classmethod
    def get_index_url(cls):
        return  reverse('posts.index')

