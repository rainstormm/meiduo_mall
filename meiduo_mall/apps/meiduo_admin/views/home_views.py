from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from users.models import User
from orders.models import OrderInfo
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
import pytz
from django.conf import settings
from meiduo_admin.serializers.home_serializers import *
from rest_framework.permissions import IsAdminUser

class HomeView(ViewSet):
    permission_classes = [IsAdminUser]

    @action(methods=["get"],detail=False)
    def total_count(self,request):
        count=User.objects.filter(is_active=True).count()
        # date=timezone.now().date()
        date=timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)).date()
        return Response(
            {
                "count": count,
                "date": date,
            }
        )

    @action(methods=["get"],detail=False)
    def day_increment(self,request):
        curr_date=timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE))
        count=User.objects.filter(date_joined__gte=curr_date.replace(hour=0,minute=0,second=0)).count()
        return Response({
            "count":count,
            "date": curr_date.date()
        })

    @action(methods=["get"],detail=False)
    def day_active(self,request):
        curr_date=timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE))
        count=User.objects.filter(last_login__gte=curr_date.replace(hour=0,minute=0,second=0)).count()
        return Response({
            "count":count,
            "date":curr_date.date()
        })

    @action(methods=["get"],detail=False)
    def day_orders(self,request):
        curr_date = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE))
        # user_list=[]
        # orders=OrderInfo.objects,filter(create_time__gte=curr_date.replace(hour=0,minute=0,second=0))
        # for order in orders:
        #     user_list.append(order.user)
        # user_list=set(user_list)
        # count=len(user_list)

        user_list=User.objects.filter(orders__create_time__gte=curr_date.replace(hour=0,minute=0,second=0))
        #(orderinfo_set__)
        user_list = set(user_list)
        count=len(user_list)
        return Response({
            "count":count,
            "date":curr_date.date()
        })


    @action(methods=["get"],detail=False)
    def month_increment(self,request):

        curr_date=timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0,minute=0,second=0)
        start_date=curr_date-timedelta(days=29)
        res=[]
        for index in range(30):
            calc_date=start_date+timedelta(days=index)
            count=User.objects.filter(date_joined__gte=calc_date,date_joined__lt=calc_date+timedelta(days=1)).count()
            res.append({
                    "count": count,
                    "date":calc_date.date()
                })

        return Response(res)

    @action(methods=["get"],detail=False)
    def goods_day_views(self,request):
        goods_visit_queryset=GoodsVisitCount.objects.filter(create_time__gte=timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0,minute=0,second=0))
        serializer=GoodsVisitSerializer(goods_visit_queryset,many=True)
        return Response(serializer.data)



