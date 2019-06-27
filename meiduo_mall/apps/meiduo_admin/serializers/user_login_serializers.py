from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField()
    def validate(self,attrs):
        # username=attrs.get("username")
        # password=attrs.get("password")
        # authenticate(username=username,password=password)
        user=authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("用户认证失败！")

        payload=jwt_payload_handler(user)
        token=jwt_encode_handler(payload)
        return {
            "user":user,
            "jwt_token":token
        }

