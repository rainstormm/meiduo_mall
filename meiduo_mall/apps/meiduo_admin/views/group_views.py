from rest_framework.decorators import action
from rest_framework.response import Response

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.group_serializers import *
from rest_framework.viewsets import ModelViewSet

class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPage

    def get_queryset(self):
        if self.action=="simple":
            return Permission.objects.all()
        return self.queryset

    def get_serializer_class(self):
        if self.action=="simple":
            return PermSimpleSerializer
        return self.serializer_class

    @action(methods=["get"],detail=False)
    def simple(self,request):
        permission_queryset=self.get_queryset()
        s=self.get_serializer(permission_queryset,many=True)
        return Response(s.data)
