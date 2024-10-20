from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, remove_perm
from authxs.models import Article

# 获取用户
lifeilong = User.objects.get(username='lifeilong')
admin = User.objects.get(username='admin')
# admin 是项目的所有者，可以默认进行编辑，不需要特别分配

# 创建一个文章并设置所有者
article = Article.objects.create(title='Python为什么这么慢？', content='因为Python是动态类型的')

# 给 lifeilong 分配该文章的编辑权限
assign_perm('change_article', lifeilong, article)

# 检查是否有 article 的权限
lifeilong.has_perm('change_article', article)  # True

# 移除该文章的权限
remove_perm('change_article', lifeilong, article)
