from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import json


# Create your views here.

def index(request):
    return render(request, template_name="index.html")


def route_params_int(request, uid: int):
    """
    接收int类型参数的视图
    :param request:
    :param uid:
    :return:
    """
    context = {"param": {"uid": uid}}
    return HttpResponse(json.dumps(context))


def route_params_str(request, name: str):
    """
    接收str类型参数的视图
    :param request:
    :param uid:
    :return:
    """
    context = {"param": {"name": name}}
    return HttpResponse(json.dumps(context))


def route_params_multi(request, name: str, version: int):
    """
    接收多个类型参数的视图
    :param request:
    :param uid:
    :return:
    """
    context = {"param": {"name": name, "version": version}}
    return HttpResponse(json.dumps(context))


def route_alias(request):
    """
    别名
    :param request:
    :param uid:
    :return:
    """
    context = {"param": "别名"}
    return HttpResponse(json.dumps(context, ensure_ascii=False))


def route_reflect(request):
    """
    别名
    :param request:
    :param uid:
    :return:
    """
    # context = {"param": "别名"}
    # return HttpResponse(json.dumps(context, ensure_ascii=False))
    print(reverse("alias"))
    return redirect(reverse("alias"))
