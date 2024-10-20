from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        permissions = [
            ('publish_article', 'Can publish articles'),
            ('archive_article', 'Can archive articles'),
        ]
