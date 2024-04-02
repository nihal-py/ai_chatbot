from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('chatbot', views.chatbot, name='chatbot'),

    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),

    path('SignOut2', views.SignOut2, name='SignOut2'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_history', views.user_history, name='user_history'),
    path('delete_chat/<int:pk>', views.delete_chat, name='delete_chat'),




]