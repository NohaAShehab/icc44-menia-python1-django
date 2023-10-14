from django.urls import path
from tracks.views import index, create, ShowTrack,EditTrackView
urlpatterns = [
    path('index', index, name='tracks.index'),
    path('create', create, name='tracks.create'),
    # path('<int:id>/edit', edit, name='tracks.edit'),
    path('<int:id>/edit', EditTrackView.as_view(), name='tracks.edit'),

    path('<int:id>', ShowTrack.as_view(), name='tracks.show')

]
