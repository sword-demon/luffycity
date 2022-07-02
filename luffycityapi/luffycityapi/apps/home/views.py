from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection

# 日志引入
import logging

logger = logging.getLogger("django")


class HomeAPIView(APIView):
    def get(self, request):
        """
        测试代码
        :param request:
        :return:
        """
        # 测试日志功能
        # logger.info("测试代码")
        # logger.error("测试代码")
        # logger.warn("测试代码")
        # print("hello")
        redis = get_redis_connection("sms_code")
        # print(1/0)
        # brother = ["张飞", "关羽", "刘备"]
        brother = redis.lrange("brother", 0, -1)
        return Response(brother, status.HTTP_200_OK)
