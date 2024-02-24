#Exercises 1;
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)


#Exercises 2;
from datetime import date, timedelta
dt = date.today() - timedelta(1)
zt = date.today() + timedelta(1)
print("Yesterday:",dt)
print("Today:",date.today())
print("Tomorrow:", zt)

#EXercises 3;
import datetime
x = datetime.datetime.now().replace(microsecond=0)
print(x)

#Exercises 4;
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

