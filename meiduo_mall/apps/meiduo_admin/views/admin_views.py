from rest_framework.decorators import action
from rest_framework.response import Response

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.admin_serializers import *
from rest_framework.viewsets import ModelViewSet

class AdminViews(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    pagination_class = MyPage

    @action(methods=["get"],detail=False)
    def simple(self,request):
        group_queryset=Group.objects.all()
        s=AdminGroupSerializer(group_queryset,many=True)
        return Response(s.data)