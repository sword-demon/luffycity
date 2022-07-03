# -*- coding: utf8 -*-
# @Time    : 2022/7/3 18:18
# @Author  : wxvirus
# @File    : views.py
# @Software: PyCharm
# 视图基类
import constants
from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CacheListAPIView(ListAPIView):
    """
    列表视图缓存基类
    """
    @method_decorator(cache_page(constants.HOME_PAGE_CACHE_TIME))
    def get(self, request, *args, **kwargs):
        # 重写ListAPIView 的get 方法 仅仅装饰而已
        return super().get(request, *args, **kwargs)
