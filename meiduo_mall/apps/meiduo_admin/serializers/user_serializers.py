from users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id",
                "username",
                "mobile",
                "email",
                "password"]
        extra_kwargs={
            "id":{"read_only":True},
            "password":{"write_only":True}
        }

    def create(self, validated_data):
        # password=validated_data["password"]
        # validated_data["password"]=make_password(password)
        # validated_data["is_staff"]=True
        # return self.Meta.model.objects.create(**validated_data)
        return self.Meta.model.objects.create_superuser(**validated_data)

