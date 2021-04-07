from django.urls import path
from net.views import index_view, individual_net_view, net_main_view
from net_user_app.views import subscribe_net


urlpatterns = [
    path('', index_view, name='Homepage'),
    path('nets/<str:net_title>/', individual_net_view),   
    path('newnet/', net_main_view, name='new_net'),
    path('subscribe/<str:net_title>/<int:post_id>/', subscribe_net)
]