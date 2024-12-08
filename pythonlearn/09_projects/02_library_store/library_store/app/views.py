from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import User

from rest_framework.permissions import BasePermission


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # 允许任何人访问
@authentication_classes([])  # 禁用身份验证
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    # confirmpassword = request.data.get('confirmpassword')

    # if not username or not password:
    #     return Response({"error": "请输入用户名或密码。"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "用户名已被占用。"}, status=status.HTTP_400_BAD_REQUEST)

    user = User(username=username, password=make_password(password))
    user.save()
    return Response({"message": "用户注册成功。"}, status=status.HTTP_201_CREATED)