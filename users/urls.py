# coding=gbk

"""ΪӦ�ó���users����URLģʽ"""
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

LoginView.template_name = 'users/login.html'
urlpatterns = [
    # ��¼����
    path('login/', LoginView.as_view(), name='login'),
    # ע��
    path('logout/', views.logout_view, name='logout'),
    # ע��ҳ��
    path('register/', views.register, name='register'),
]

app_name = 'users'
