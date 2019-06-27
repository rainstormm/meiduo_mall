from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import GoodsChannel,GoodsChannelGroup
from meiduo_admin.serializers.channel_serializers import *
from meiduo_admin.pages import MyPage

class ChannelViewSet(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class = ChannelSerializer
    pagination_class = MyPage

    @action(methods=["get"],detail=False)
    def channel_types(self,request):
        group_queryset=GoodsChannelGroup.objects.all()
        s=ChannelGroupSerializer(group_queryset,many=True)
        return Response(s.data)


    @action(methods=["get"],detail=False)
    def categories(self,request):
        category_queyset=GoodsCategory.objects.filter(parent=None)
        s=ChannelCategorySerializer(category_queyset,many=True)
        return Response(s.data)