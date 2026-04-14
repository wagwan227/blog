from django.urls import path
from login import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('add_user/', views.add_user, name='add_user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
