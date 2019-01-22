# coding=gbk

"""����learning_logs��URLģʽ"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    #��ҳ
    path('', views.index, name='index'),
    # ��ʾ���е�����
    path('topics/', views.topics, name='topics'),
    # �ض��������ϸҳ��
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    # ����������������ҳ
    re_path('new_topic/', views.new_topic, name='new_topic'),
    # �����������Ŀ��ҳ��
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    # ���ڱ༭��Ŀ��ҳ��
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, \
            name='edit_entry'),
]
app_name = 'learning_logs'
