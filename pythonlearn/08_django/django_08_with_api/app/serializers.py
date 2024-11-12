from rest_framework import serializers
from app.models import *


class BookSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Book
        fields = '__all__'
