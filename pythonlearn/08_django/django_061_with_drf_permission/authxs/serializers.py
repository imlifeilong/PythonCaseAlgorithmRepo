from rest_framework import serializers
from authxs.models import CommonBook, VIPBook, SVIPBook


# 数据进行序列化
class CommonBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonBook
        fields = "__all__"


class VIPBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIPBook
        fields = "__all__"


class SVIPBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SVIPBook
        fields = "__all__"
