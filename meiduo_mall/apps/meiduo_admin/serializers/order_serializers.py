from rest_framework import serializers
from orders.models import OrderInfo,OrderGoods
from goods.models import SKU


class OrderSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'create_time',
            'status',
        ]

class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'name',
            'default_image'
        ]


class OrderGoodsSerializer(serializers.ModelSerializer):
    sku = SKUSimpleSerializer(read_only=True)
    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderDetailSerializer(serializers.ModelSerializer):
    skus = OrderGoodsSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = OrderInfo
        fields = "__all__"