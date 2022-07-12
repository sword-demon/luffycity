# -*- coding: utf8 -*-
# @Time    : 2022/7/9 21:29
# @Author  : wxvirus
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
# 引入jwt的登录视图
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # name 提供url别名 前后端分离里相对的比较少使用 删不删无所谓
    path('login/', obtain_jwt_token, name='login'),
]
