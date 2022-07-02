# -*- coding: utf8 -*-
# @Time    : 2022/7/2 21:55
# @Author  : wxvirus
# @File    : urls.py
# @Software: PyCharm
# 路由文件
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.HomeAPIView.as_view())
]