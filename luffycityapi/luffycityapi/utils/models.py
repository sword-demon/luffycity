# -*- coding: utf8 -*-
# @Time    : 2022/7/3 14:28
# @Author  : wxvirus
# @File    : models.py
# @Software: PyCharm
from django.db import models


class BaseModel(models.Model):
    """
    公共模型
    """
    name = models.CharField(max_length=255, default='', verbose_name='名称/标题')
    orders = models.IntegerField(default=0, verbose_name='排序')
    is_show = models.BooleanField(default=True, verbose_name='是否在前端显示')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除了')
    # auto_now_add 当数据被创建时，以当前时间作为默认值写入
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    # auto_now 当数据被更新时，以当前时间作为值写入当前字段
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 设置当前模型并未真正的模型，而是一种保存公共代码的抽象模型类
        # 这种模型在数据迁移中不会被当成数据模型来创建数据表
        abstract = True
