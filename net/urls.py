from django.urls import path
from net import views

urlpatterns = [
    path('', views.index_view, name='Homepage'),
    path('nets/<str:net_title>/', views.individual_net_view, name="Individual Net Page"),   
    path('newnet/', views.create_net_view, name='Make Net'),
    path('subscribe/<str:net_title>/', views.subscribe_net, name="Subscribe"),
    path('editmoderators/<str:net_title>/', views.change_moderators, name="Edit Moderators"),
    path('editsubscribers/<str:net_title>/', views.change_subscribers, name="Edit Subscribers"),
    path('searchrequests/', views.search_request_view, name="Search Request")
]

handler404 = 'net.views.error_404_view'
handler500 = 'net.views.error_500_view'