from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
    path('makeallread/', views.mark_as_read, name="Mark all as Read"),
]
