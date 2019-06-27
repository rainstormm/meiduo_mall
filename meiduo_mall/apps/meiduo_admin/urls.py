
from django.conf.urls import url, include

from meiduo_admin.views.brand_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *
from meiduo_admin.views.perm_views import *
from .views.user_login_views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.utils import jwt_response_payload_handler
from .views.home_views import *
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.user_views import *
from meiduo_admin.views.sku_views import *

from meiduo_admin.views.spu_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.channel_views import *
from meiduo_admin.views.group_views import *
from meiduo_admin.views.admin_views import *

urlpatterns = [
    # url(r'^authorizations/$', UserLoginView.as_view())

    # obtain_jwt_token给我们返回给前端的数据只有token，没有额外的数据
    url(r'^authorizations/$', obtain_jwt_token),
    #url(u"^statistical/total_count/$",include(HomeView.as_view("get":"total_count")))
    url(r'^users/$',UserView.as_view()),
    url(r'^skus/$', SKUView.as_view({"get":"list","post":"create"})),
    url(r'^skus/(?P<pk>\d+)/$',SKUView.as_view({"delete":"destroy","get":"retrieve","put":"update"})),
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$',SpecOptView.as_view()),
    url(r'^goods/$',SPUViews.as_view({"get":"list","post":"create"})),
    url(r'^goods/(?P<pk>\d+)/$',SPUViews.as_view({"delete":"destroy","get":"retrieve","put":"update"})),
    url(r'^goods/brands/simple/$',SPUBrandSimpleViews.as_view()),
    url(r'^goods/channel/categories/$',SPUCategoryViews.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', SPUCategoryViews.as_view()),
    # url(r'^goods/specs/$', SpecViewSet.as_view({"get":"list", "post":"create"})),
    # url(r'^goods/spces/(?P<pk>\d+)/$', SpecViewSet.as_view({"delete": "destroy", "put": "update","get":"retrieve"})),
    url(r'^specs/options/$',OptionViewSet.as_view({"get":"list","post":"create"})),
    url(r'^specs/options/(?P<pk>\d+)/$', OptionViewSet.as_view({"delete": "destroy", "get": "retrieve","put":"update"})),

    url(r'^goods/specs/simple/$', SpecSimpleView.as_view()),
    url(r'^goods/channels/$',ChannelViewSet.as_view({"get":"list","post":"create"})),
    url(r'^goods/channels/(?P<pk>\d+)/$', ChannelViewSet.as_view({"get": "retrieve", "put": "update","delete":"destroy"})),

    url(r'^goods/categories/$',ChannelViewSet.as_view({"get":"categories"})),
    url(r'^goods/channel_types/$', ChannelViewSet.as_view({"get": "channel_types"})),


    url(r'^goods/brands/$', BrandViewSet.as_view({"get": "list", 'post': 'create'})),
    # 删除对象
    url(r'^goods/brands/(?P<pk>\d+)/$', BrandViewSet.as_view({'delete': 'destroy','get':'retrieve','put':'update'})),
    url(r'^skus/images/$', ImageViewSet.as_view( {"get": "list", 'post': 'create'})),
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({'get': 'retrieve', 'delete': 'destroy','put':'update'})),
    url(r'^skus/simple/$', ImageViewSet.as_view({"get":"simple"})),
    url(r'^orders/$', OrderViewSet.as_view({"get":"list"})),
    url(r'^orders/(?P<pk>\d+)/$', OrderViewSet.as_view({"get":"retrieve"})),
    url(r'^orders/(?P<pk>\d+)/status/$', OrderViewSet.as_view({"put":"partial_update"})),
    url(r'^permission/perms/$', PermViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^permission/perms/(?P<pk>\d+)/$', PermViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',"put":"update"})),

    url(r'^permission/content_types/$', PermViewSet.as_view({'get': 'content_types'})),
    url(r'^permission/groups/$',GroupViews.as_view({"get":"list","post":"create"})),
    url(r'^permission/groups/(?P<pk>\d+)/$', GroupViews.as_view({"get": "retrieve", "delete": "destroy","put":"update"})),

    url(r'^permission/simple/$',GroupViews.as_view({"get":"simple"})),
    url(r'^permission/admins/$',AdminViews.as_view({"get":"list","post":"create"})),
    url(r'^permission/groups/simple/$',AdminViews.as_view({"get":"simple"})),
    url(r'^permission/admins/(?P<pk>\d+)/$', AdminViews.as_view({"get": "retrieve", "delete": "destroy","put":"update"})),

]




router=SimpleRouter()
router.register(prefix="statistical",viewset=HomeView,base_name="home")
router.register(prefix='goods/specs', viewset=SpecViewSet, base_name='specs')
urlpatterns+=router.urls

# from fdfs_client.client import Fdfs_client
# conn=Fdfs_client('./meiduo_mall/client.conf')