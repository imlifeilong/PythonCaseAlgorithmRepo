from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(max_length=64)
    title = models.CharField(max_length=10)

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


"""
authxs.Role.permission: (fields.W340) null has no effect on ManyToManyField.
在 Django 中，ManyToManyField 字段不能使用 null=True。null 选项对 ManyToManyField 没有影响，因为多对多关系是通过中间表存储的，不直接在主模型表中使用 NULL。
"""


class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=10)
    permission = models.ManyToManyField(Permission, verbose_name='permission', blank=True)

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


"""
https://github.com/labd/django-cognito-jwt/issues/20
auth.User.groups: (fields.E304) Reverse accessor for 'auth.User.groups' clashes with reverse accessor for 'authxs.User.groups'.
需要在setting中重载AUTH_USER_MODEL
AUTH_USER_MODEL = 'authxs.User'
"""

"""
设置普通用户的密码需要通过User.objects.get(username='lifeilong').set_password('admin123!')进行设置
admin 后台设置的密码是没有加密的 
"""


class User(AbstractUser):
    """
    用户表
    """
    roles = models.ManyToManyField(Role, related_name="roles_for_user", verbose_name='roles', blank=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.username}>"


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = verbose_name
        permissions = [
            ("can_review_article", "Can review article")
        ]
