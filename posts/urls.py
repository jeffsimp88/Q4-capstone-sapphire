from django.urls import path
from posts import views


urlpatterns = [
    path('makepost/', views.post_form_view, name='make post'),
]