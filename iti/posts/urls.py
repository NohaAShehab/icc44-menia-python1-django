from django.urls import path
from django.contrib.auth.decorators import login_required

from posts.views import  (PostCreateView, PostListView, PostEditView,
                          PostDetailView, PostDeleteView)
urlpatterns = [
    path('create', login_required(PostCreateView.as_view()),name='posts.create'),
    path('', PostListView.as_view(),name='posts.index'),
    path('<int:pk>/edit',PostEditView.as_view(), name='posts.edit'),
    path('<int:pk>', PostDetailView.as_view(), name='posts.show'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='posts.delete')
]