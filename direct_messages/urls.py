from django.urls import path
from direct_messages import views

urlpatterns = [
    path('messages/', views.message_view, name="Direct Messages"),

]