from django.urls import path
from tracks.views import index, create, edit
urlpatterns = [
    path('index', index, name='tracks.index'),
    path('create', create, name='tracks.create'),
    path('<int:id>/edit', edit, name='tracks.edit')
]
