from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.spec_serializers import *
from rest_framework.viewsets import ModelViewSet
from goods.models import SPUSpecification

class SpecViewSet(ModelViewSet):

    queryset = SPUSpecification.objects.all()
    serializer_class = SpecSerializer
    pagination_class = MyPage