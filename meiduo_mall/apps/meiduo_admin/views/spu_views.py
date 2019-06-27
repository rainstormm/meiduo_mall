from rest_framework.generics import ListAPIView

from goods.models import SPU
from meiduo_admin.serializers.spu_serializers import *
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.pages import MyPage

class SPUViews(ModelViewSet):
    queryset=SPU.objects.all()
    serializer_class = SPUModelSerializer
    pagination_class = MyPage
    def get_queryset(self):
        keyword=self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(keyword=keyword)
        return self.queryset.all()



class SPUBrandSimpleViews(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = SPUBrandSimpleSerialzer

class SPUCategoryViews(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = SPUCategorySerializer
    def get_queryset(self):
        pk=self.kwargs.get("pk")
        if pk:
            return self.queryset.filter(parent_id=pk)

        return self.queryset.filter(parent=None)