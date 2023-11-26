from django.urls import path
from . import views
from .views import CreatePostView, EditPostView, DetailView, DeletePostView

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail_page'),
    path('detail/<int:pk>/remove', DeletePostView.as_view(), name='delete_page')
]

