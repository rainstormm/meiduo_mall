from rest_framework import serializers
from goods.models import Brand
from fdfs_client.client import Fdfs_client
from django.conf import settings



class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'logo',
            'first_letter'
        ]
    def create(self,validated_data):
        logo=validated_data["logo"]
        conn=Fdfs_client(settings.FDFS_CONFIG_PATH)
        content=logo.read()
        res=conn.upload_by_buffer(content)
        if not res.get("Status")=="Upload successed.":
            raise serializers.ValidationError("upload fail")
        url=res.get("Remote file_id")
        validated_data["logo"]=url
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logo = validated_data["logo"]
        conn = Fdfs_client(settings.FDFS_CONFIG_PATH)
        content = logo.read()
        res = conn.upload_by_buffer(content)
        if not res.get("Status") == "Upload successed.":
            raise serializers.ValidationError("upload fail")
        url = res.get("Remote file_id")
        instance.logo = url
        instance.save()
        return instance