from rest_framework import serializers
from goods.models import SPU,Brand,GoodsCategory



class SPUModelSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField()
    category1_id=serializers.IntegerField()
    category2_id=serializers.IntegerField()
    category3_id=serializers.IntegerField()
    class Meta:
        model=SPU
        exclude=["category1","category2","category3"]


class SPUBrandSimpleSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=["id","name"]

class SPUCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields=["id","name"]