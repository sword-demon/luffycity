# -*- coding: utf8 -*-
# @Time    : 2022/7/31 15:14
# @Author  : wxvirus
# @File    : authenticate.py
# @Software: PyCharm

from rest_framework_jwt.utils import jwt_payload_handler as payload_handler


def jwt_payload_handler(user):
    """
    自定义载荷信息
    :param user: 用户模型实例对象
    :return:
    """
    # 先让jwt模块生成自己的载荷信息
    payload = payload_handler(user)
    # 追加自己要返回的内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname

    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload
