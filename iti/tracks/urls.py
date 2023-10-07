from django.urls import path
from tracks.views import index
urlpatterns = [
    path('index', index, name='tracks.index')
]
