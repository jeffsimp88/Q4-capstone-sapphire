from django.urls import path
from posts import views


urlpatterns = [
    path('posts/<int:post_id>/', views.individual_post_view, name='individual post'),
    path('makepost/<net_title>/', views.create_post_view, name='make post'),
    path('makecomment/<int:post_id>/', views.post_comment_view, name='make comment'),
    path('upvote/<int:post_id>/', views.upvotes_view, name='upvotes'),
    path('downvote/<int:post_id>/', views.downvotes_view, name='downvotes'),
]