from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


class User(AbstractUser):
    GENDER = {
        ("1", "男"),
        ("2", "女")
    }
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    gender = models.CharField(max_length=10, choices=GENDER, default="1", verbose_name="性别")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="注册时间")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
