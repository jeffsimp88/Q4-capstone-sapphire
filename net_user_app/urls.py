from django.urls import path
from net_user_app import views

urlpatterns = [
    path('users/<username>/', views.profile_view, name="User Profile"),
]