from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(max_length=256)
    name = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name


class Role(models.Model):
    """
    角色表
    """

    name = models.CharField(max_length=10)
    permission = models.ManyToManyField(Permission, verbose_name='permission', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = verbose_name


class User(AbstractUser):
    """
    用户表
    """
    phone = models.CharField(max_length=20, blank=True, null=True)
    roles = models.ManyToManyField(Role, related_name="user", verbose_name='roles', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class Classified(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


class Label(models.Model):
    """
    标签
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


class Books(models.Model):
    """
    图书
    """
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
    )
    id = models.BigAutoField(primary_key=True)
    """
    ForeignKey 外键
    on_delete=models.CASCADE 级联删除，当关联的Classified记录被删除时，相关的书籍也会被删除
    related_name='books'  可以从Classified对象反向查询所有与之关联的Books对象
    """
    classified = models.ForeignKey(Classified, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='books')
    label = models.ManyToManyField(Label, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to='icon/', null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    translator = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    publisher = models.CharField(max_length=512, blank=True, null=True)
    release_date = models.DateField(null=True)
    pages = models.IntegerField(default=0)
    # DecimalField类型，设置最大数字位数和小数位数
    price = models.DecimalField(max_length=50, decimal_places=2, max_digits=10, blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
