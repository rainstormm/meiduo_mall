from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User

from django.contrib.auth.models import Group

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","mobile","groups","password","user_permissions"]
        extra_kwargs={"password":{"write_only": True},}

    def create(self, validated_data):
        # pw = validated_data["password"]
        # validated_data["password"] = make_password(pw)
        # validated_data["is_staff"] = True
        # return super().create(validated_data)
        groups=validated_data.pop("groups")
        user_permissions=validated_data.pop("user_permissions")
        admin_user=User.objects.create_superuser(**validated_data)
        admin_user.groups.set(groups)
        admin_user.user_permissions.set(user_permissions)
        return admin_user

    def update(self, instance, validated_data):
        pw=validated_data.get("password")
        if pw:
            validated_data["password"]=make_password(pw)
        else:
            validated_data["password"]=instance.password
        return super().update(instance,validated_data)


class AdminGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=["id","name"]




