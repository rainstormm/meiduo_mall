from goods.models import GoodsVisitCount
from rest_framework import serializers

class GoodsVisitSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model= GoodsVisitCount
        fields=["category","count"]