from rest_framework.viewsets import ModelViewSet
from orders.models import OrderInfo
from meiduo_admin.serializers.order_serializers import *
from meiduo_admin.pages import MyPage


class OrderViewSet(ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSimpleSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword=self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(order_id__contains=keyword)
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action=="retrieve":
            return OrderDetailSerializer
        return self.serializer_class
