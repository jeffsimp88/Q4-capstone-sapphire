from django.urls import path
from posts import views


urlpatterns = [
    path('makecomment/<int:post_id>/', views.post_comment_view, name='make comment'),
]