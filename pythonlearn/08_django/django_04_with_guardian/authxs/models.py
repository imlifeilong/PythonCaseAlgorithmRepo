from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_review_article", "Can review article")
        ]
