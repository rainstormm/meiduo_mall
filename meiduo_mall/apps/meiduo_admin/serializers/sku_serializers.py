from rest_framework import serializers
from goods.models import SKU,SKUSpecification,GoodsCategory,SPU,SPUSpecification,SpecificationOption


class SKUSpecModelSerializer(serializers.ModelSerializer):
    spec_id=serializers.IntegerField()
    option_id=serializers.IntegerField()
    class Meta:
        model=SKUSpecification
        fields=["spec_id","option_id"]


class SKUModelSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    category_id=serializers.IntegerField()
    spu=serializers.StringRelatedField()
    spu_id=serializers.IntegerField()
    specs=SKUSpecModelSerializer(many=True)

    class Meta:
        model=SKU
        fields="__all__"

    def create(self, validated_data):
        spec_option=validated_data.get("specs")
        sku=super().create(validated_data)
        for temp in spec_option:
            temp["sku_id"]=sku.id
            SPUSpecification.objects.create(**temp)
        return sku

    def update(self, instance, validated_data):
        spec_option=validated_data.get("specs")

        for temp in spec_option:
            m=SPUSpecification.objects.get(spu_id=instance.id,spec_id=temp["spec_id"])
            m.option_id=temp["option_id"]
            m.save()
        return super().update(instance,validated_data)

class GoodsCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields=["id","name"]


class SPUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=SPU
        fields=["id","name"]

class SpecOptSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpecificationOption
        fields=["id","value"]

class SPUSpecModelSerializer(serializers.ModelSerializer):
    spu=serializers.StringRelatedField()
    spu_id=serializers.IntegerField()
    options=SpecOptSerializer(many=True,read_only=True)
    class Meta:
        model=SPUSpecification
        fields=["id","name","spu","spu_id","options"]

