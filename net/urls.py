from django.urls import path
from net import views


urlpatterns = [
    path('', views.index_view, name='Homepage'),
    path('nets/<str:net_title>/', views.individual_net_view)
]