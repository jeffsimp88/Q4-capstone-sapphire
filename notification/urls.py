from django.urls import path
from notification import views


from . import views

urlpatterns = [
    path("notifications/", views.notifications, name="notifications"),
]
