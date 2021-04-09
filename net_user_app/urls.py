from django.urls import path
from net_user_app import views

urlpatterns = [
    path('users/<username>/', views.profile_view, name="User Profile"),
    path('changetheme/', views.change_theme, name="Change Theme"),
    path('follow/<username>/', views.follow_user, name="Follow User"),
    path('updateuser/<int:user_id>/', views.update_user, name="Update User"),
]