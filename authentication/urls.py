from django.urls import path
from authentication import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index_view, name='index'),
]
# handler404 = 'net.views.error_404_view'