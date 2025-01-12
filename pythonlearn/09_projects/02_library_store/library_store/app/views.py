from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import User

from app.serializers import BooksSerializer

from rest_framework.permissions import BasePermission

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # if serializer.is_valid():
        #     user = serializer.object.get("username") or request.user
        #     token = jwt_encode_handler(jwt_payload_handler(user))

        return Response({"status": True, "data": {"username": "admin", "token": "9tqoF8c2yVefD0j2LgImAJ5UuRvxyUBl"}},
                        status=status.HTTP_200_OK)


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


class CreateAPIView(APIView):
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
