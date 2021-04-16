from django.urls import path, include
from notification import views
from .views import notifications

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
]
