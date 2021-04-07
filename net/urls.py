from django.urls import path
from net import views

urlpatterns = [
    path('', views.index_view, name='Homepage'),
    path('nets/<str:net_title>/', views.individual_net_view, name="Individual Net Page"),   
    path('newnet/', views.net_main_view, name='Make Net'),
    path('subscribe/<str:net_title>/', views.subscribe_net, name="Subscribe"),
]