import json

from django.contrib import auth
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from authxs.utils import get_token

# 引入drf相关模块
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import exceptions

from authxs.models import *
from authxs.serializers import *


#
# def login(request):
#     print(request.body)
#     return HttpResponse(json.dumps({"msg": "everything ok."}))


class AuthView(APIView):

    def post(self, request):
        ret = {'code': 1000, 'msg': '登录成功！'}
        try:
            username = request._request.POST.get('username')
            password = request._request.POST.get('password')
            # auth.authenticate 检查用户提交的用户名和密码是否匹配存储在数据库中的用户记录，并返回一个 User 对象
            # 因为 密码时加密的需要使用 auth.authenticate 验证
            authres = auth.authenticate(username=username, password=password)
            if authres:
                # auth.login 在当前会话中标记用户为已登录状态 会将该用户与当前会话（通常是基于 HTTP cookies 的会话）关联起来
                # auth.login(request, authres)
                token_salt = f"{authres.username}+{authres.password}"
                token = get_token(token_salt)
                Token.objects.update_or_create(user=authres, defaults={'token': token})
                ret['token'] = token
            else:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'

        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)


class Authtication(object):
    def authenticate(self, request):
        # 验证是否已经登录,函数名必须为：authenticate
        token = request._request.GET.get('token')
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败。')
        # 在rest_framework内部会将以下两个元素赋值到request，以供后续使用
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        # 这个函数可以没内容，但是必须要有
        pass


class VIPAuthtication(object):
    """
    验证VIP权限
    """

    def has_permission(self, request, view):
        if request.user.usertype < 2:
            return False
        return True


class SVIPAuthtication(object):
    """
    验证SVIP权限
    """

    def has_permission(self, request, view):
        if request.user.usertype < 3:
            return False
        return True


class CommonBookView(APIView):
    """
    登录后即可访问的内容资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    authentication_classes = [Authtication, ]

    def get(self, request):
        video_list = CommonBook.objects.all()
        ret = CommonBookSerializer(video_list, many=True)
        return Response(ret.data)


class VIPBookView(APIView):
    """
    vip可访问的资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    authentication_classes = [Authtication, ]
    permission_classes = [VIPAuthtication]

    def get(self, request):
        video_list = VIPBook.objects.all()
        re = VIPBookSerializer(video_list, many=True)
        return Response(re.data)


class SVIPBookView(APIView):
    """
    vip可访问的资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    authentication_classes = [Authtication, ]
    permission_classes = [SVIPAuthtication]

    def get(self, request):
        video_list = SVIPBook.objects.all()
        re = SVIPBookSerializer(video_list, many=True)
        return Response(re.data)
