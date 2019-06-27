from rest_framework import serializers
from goods.models import SKUImage,SKU
from fdfs_client.client import Fdfs_client
from django.conf import settings



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKUImage
        fields = [
            'id',
            'sku', # PrimaryKeyRelatedField(queryset=SKU.objects.all())
            'image'
        ]


    def create(self, validated_data):

        image = validated_data.pop('image')
        conn = Fdfs_client(settings.FDFS_CONFIG_PATH)
        content = image.read()  # bytes
        result = conn.upload_by_buffer(content)
        if not result.get("Status") == "Upload successed.":
            raise serializers.ValidationError("上传失败")
        url = result.get("Remote file_id")
        validated_data['image'] = url
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image')
        conn = Fdfs_client(settings.FDFS_CONFIG_PATH)
        content = image.read()  # bytes
        result = conn.upload_by_buffer(content)
        if not result.get("Status") == "Upload successed.":
            raise serializers.ValidationError("上传失败")
        url = result.get("Remote file_id")
        validated_data['image'] = url
        return super().update(instance, validated_data)


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'id',
            'name'
        ]