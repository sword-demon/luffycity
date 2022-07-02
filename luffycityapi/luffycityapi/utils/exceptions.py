# -*- coding: utf8 -*-
# @Time    : 2022/7/2 18:21
# @Author  : wxvirus
# @File    : exceptions.py
# @Software: PyCharm
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging

# 日志记录对象
logger = logging.getLogger('django')


def custom_exception_handler(exc, context):
    """
    自定义异常
    :param exc: 异常类
    :param context: 抛出异常的执行上下文
    :return: Response响应对象
    """

    # 调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)

    if response is None:
        view = context['view']
        # 判断是否发生了数据库异常
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error('[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
