from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户表
    """
    user_type_chioces = (
        (1, "普通会员"),
        (2, "大会员"),
        (3, "超级会员"),
    )
    usertype = models.IntegerField(choices=user_type_chioces, default=1)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.username}>"


# class Token(models.Model):
#     """
#     token表
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=64)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = 'token表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.user.username


class CommonBook(models.Model):
    """
    普通内容
    """
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=200, verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '普通内容表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class VIPBook(models.Model):
    """
    大会员内容
    """
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=200, verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '大会员内容表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SVIPBook(models.Model):
    """
    超级会员内容
    """
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=200, verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '超级会员内容表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
