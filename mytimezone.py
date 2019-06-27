from datetime import datetime,timedelta
import pytz

#time in python
mytzinfo=pytz.timezone("Asia/Shanghai")
mytime=datetime(year=2019,month=6,day=18,hour=17,minute=30,second=15,tzinfo=mytzinfo) #timezone object

yesterday=mytime-timedelta(days=1)
print(yesterday)

#time switch
utc_zone=pytz.timezone("UTC")
utc_time=mytime.astimezone(tz=utc_zone)
