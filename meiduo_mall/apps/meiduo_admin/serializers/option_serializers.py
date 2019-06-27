
from goods.models import SpecificationOption,SPUSpecification
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    spec = serializers.StringRelatedField()
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = ['id', 'value', 'spec', 'spec_id']

class SpecSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=SPUSpecification
        fields=["id","name"]
