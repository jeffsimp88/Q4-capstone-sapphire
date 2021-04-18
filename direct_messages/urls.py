from django.urls import path
from direct_messages import views

urlpatterns = [
    path('messages/', views.message_view, name="Direct Messages"),
    path('messages/<username>/', views.user_message_view, name="User Messages"),
    path('sendmessage/<username>/', views.create_message, name="Send Message"),
]