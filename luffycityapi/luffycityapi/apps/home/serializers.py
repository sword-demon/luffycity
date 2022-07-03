# -*- coding: utf8 -*-
# @Time    : 2022/7/3 14:47
# @Author  : wxvirus
# @File    : serializers.py
# @Software: PyCharm
# 序列化器配置
from rest_framework import serializers
from .models import Nav, Banner


class NavModelSerializer(serializers.ModelSerializer):
    """
    导航菜单的序列化器
    """

    class Meta:
        model = Nav
        fields = ["id", "name", "link", "is_http"]


class BannerModelSerializer(serializers.ModelSerializer):
    """
    轮播广告的序列化器
    """

    class Meta:
        model = Banner
        fields = ["id", "name", "link", "is_http", "image"]
