import json
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from guardian.decorators import permission_required_or_403
from authxs.models import Article


@permission_required('authxs.can_review_article')
def review_article(request):
    # 仅有权限的用户才能访问这个视图
    return HttpResponse(json.dumps({"msg": "查看所有的文章"}, ensure_ascii=False))


# 使用 Django-Guardian 的装饰器进行权限检查
@permission_required_or_403('change_article', (Article, 'pk', 'article_id'))
def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    return HttpResponse(json.dumps({"msg": {"title": article.title, "content": article.content}}, ensure_ascii=False))
