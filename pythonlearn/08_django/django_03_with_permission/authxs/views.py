import json
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Article


class ArticleListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    类视图权限权限控制
    LoginRequiredMixin：用户登录验证。
    PermissionRequiredMixin：用户权限验证。
    """
    model = Article
    permission_required = 'authxs.view_article'  # 只有分配的 view_article 权限的用户可以访问

    def get(self, request):
        return HttpResponse(json.dumps({"msg": "查看所有的文章"}, ensure_ascii=False))


@login_required
@permission_required('authxs.view_article', raise_exception=True)
def article_list(request):
    """
    函数视图权限控制

    """
    articles = Article.objects.all()
    print(articles)
    return HttpResponse(json.dumps({"msg": "查看所有的文章"}, ensure_ascii=False))


@login_required
@permission_required('authxs.delete_article', raise_exception=True)
def article_delete(request):
    """
    函数视图权限控制
    """
    articles = Article.objects.all()
    print(articles)
    return HttpResponse(json.dumps({"msg": "删除文章"}, ensure_ascii=False))


def check_user_permission_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You are not logged in")

    permissions = {}
    for p in ("authxs.delete_article", "authxs.view_article"):
        if request.user.has_perm(p):
            permissions[p] = True
        else:
            permissions[p] = False

    # 用户有权限，执行相应逻辑
    return HttpResponse(json.dumps({"msg": f"{request.user.username} 拥有的权限", "permissions": permissions},
                                   ensure_ascii=False))
