from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.user_serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from users.models import User
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from meiduo_admin.pages import MyPage



class UserView(ListAPIView,CreateAPIView): #(GenericAPIView):
    queryset=User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword=self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(username__contains=keyword)
        return self.queryset.all()


    # def get(self,request):
    #     user_queryset=self.get_queryset()
    #     page=self.paginate_queryset(user_queryset)
    #     if page:
    #         page_serializer=self.get_serializer(page,many=True)
    #         return self.get_paginated_response(page_serializer.data)
    #
    #     serializer=self.get_serializer(user_queryset,many=True)
    #     return Response(serializer.data)

