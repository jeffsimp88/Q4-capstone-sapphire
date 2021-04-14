<<<<<<< HEAD
from django.urls import path, include

from .views import notifications

urlpatterns = [
    path('', notifications, name='notifications'),
]
=======
from django.urls import path
from notification import views


from . import views

urlpatterns = [
    path("notifications/", views.notifications, name="notifications"),
]
>>>>>>> c5df4486717bb63c4069dcec2aa0d3c702466381
