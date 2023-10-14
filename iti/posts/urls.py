from django.urls import path

from posts.views import  (PostCreateView, PostListView, PostEditView,
                          PostDetailView, PostDeleteView)
urlpatterns = [
    path('create', PostCreateView.as_view(),name='posts.create'),
    path('', PostListView.as_view(),name='posts.index'),
    path('<int:pk>/edit',PostEditView.as_view(), name='posts.edit'),
    path('<int:pk>', PostDetailView.as_view(), name='posts.show'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='posts.delete')
]