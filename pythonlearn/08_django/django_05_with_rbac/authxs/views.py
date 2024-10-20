import json
from django.http import HttpResponse

from authxs import models


def check_permission(request):
    user = models.User.objects.get(username=request.user.username)
    permission_queryset = user.roles.filter(permission__isnull=False).values(
        'permission__id',
        'permission__url',
        'permission__title',
    ).distinct()
    content = {"user": user.username, "permission": list(permission_queryset)}

    return HttpResponse(json.dumps({"msg": content}, ensure_ascii=False))


def edit_article(request, article_id):
    user = models.User.objects.get(username=request.user.username)
    permission_queryset = user.roles.filter(permission__url="/edit_article/").values(
        'permission__id',
        'permission__url',
        'permission__title',
    ).distinct()

    if permission_queryset:
        content = {"user": user.username, "permission": list(permission_queryset)}
    else:
        content = {"user": user.username, "permission": "没有权限"}
    return HttpResponse(json.dumps({"msg": content}, ensure_ascii=False))


def add_article(request, article_id):
    return HttpResponse(json.dumps({"msg": f"增加 {article_id}"}, ensure_ascii=False))


def delete_article(request, article_id):
    user = models.User.objects.get(username=request.user.username)
    permission_queryset = user.roles.filter(permission__url="/delete_article/").values(
        'permission__id',
        'permission__url',
        'permission__title',
    ).distinct()

    if permission_queryset:
        content = {"user": user.username, "permission": list(permission_queryset)}
    else:
        content = {"user": user.username, "permission": "没有权限"}
    return HttpResponse(json.dumps({"msg": content}, ensure_ascii=False))


def view_article(request, article_id):
    return HttpResponse(json.dumps({"msg": f"查看 {article_id}"}, ensure_ascii=False))
