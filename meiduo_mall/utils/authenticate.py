from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
import re
from users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:

            user = User.objects.get(username=username)
        except:
            # 如果未查到数据，则返回None，用于后续判断
            try:
                user = User.objects.get(mobile=username)
            except:
                return None

        if request==None:
            if not user.is_staff:
                return None

        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None

