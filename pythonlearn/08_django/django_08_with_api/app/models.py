from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户表
    """

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class Classification(models.Model):
    list_display = ("title", "id")
    id = models.BigAutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True, default=-1)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
    )
    id = models.BigAutoField(primary_key=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_book')
    # tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    original_title = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    translator = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    press = models.CharField(max_length=50, blank=True, null=True)
    page_count = models.IntegerField(default=0)
    price = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateField(null=True)
    online_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    repertory = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    layout = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    pv = models.IntegerField(default=0)
    recommend_count = models.IntegerField(default=0)
    wish = models.ManyToManyField(User, blank=True, related_name="wish_books")
    wish_count = models.IntegerField(default=0)
    collect = models.ManyToManyField(User, blank=True, related_name="collect_books")
    collect_count = models.IntegerField(default=0)
