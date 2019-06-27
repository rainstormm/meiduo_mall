
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage,SKU
from meiduo_admin.serializers.image_serializers import *
from meiduo_admin.pages import MyPage
from rest_framework.decorators import action
from rest_framework.response import Response

# GET
# skus/images/
from meiduo_admin.serializers.image_serializers import *


class ImageViewSet(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageSerializer
    pagination_class = MyPage

    @action(methods=["get"],detail=False)
    def simple(self,request):
        sku_queryset=SKU.objects.all()
        s=SKUSimpleSerializer(sku_queryset,many=True)
        return Response(s.data)