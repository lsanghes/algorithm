# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
import time
import datetime

# get current time
dt1 = datetime.datetime.now()

# format datetime to string using strftime
print(dt1.strftime('%y/%m/%d %H:%M:%S'))
print(dt1.strftime('%b %d, %Y %H:%M:%S'))

# create datetime from string using strptime
dt2 = datetime.datetime.strptime("2016/12/31", '%Y/%m/%d')
dt2 = datetime.datetime.strptime("2016/12/31 01:30:00", '%Y/%m/%d %H:%M:%S')
print(dt2)

# get component for datetime
# print(dt1.year)
# print(dt1.month)
# print(dt1.day)
# print(dt1.hour)
# print(dt1.minute)
# print(dt1.second)

# create datetime from using int
dt3 = datetime.datetime(2016, 12, 14)
dt3 = datetime.datetime(2016, 12, 31, 1, 30, 30)
print(dt3)
