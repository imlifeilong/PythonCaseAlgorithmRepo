from django.contrib import admin
from authxs import models


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Article, ArticleAdmin)
