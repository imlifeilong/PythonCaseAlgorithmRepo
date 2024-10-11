from django.shortcuts import render

from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# 认证后可以访问的视图
@api_view(['GET'])
def protected_view(request):
    return Response({"message": "您已成功访问到受保护的视图！"}, status=200)


# 使用类视图
class ProtectedView(APIView):
    permission_classes = (IsAuthenticated,)  # 只有认证的用户可以访问

    def get(self, request):
        return Response({"message": "您已成功访问到受保护的类视图！"})


@api_view(['POST'])
def custom_jwt_login(request):
    """
    自定义 JWT 登录视图
    """
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            # 这里调用 rest_framework_jwt 提供的登录视图逻辑
            return obtain_jwt_token(request)
        else:
            return Response({"detail": "密码错误"}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"detail": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
