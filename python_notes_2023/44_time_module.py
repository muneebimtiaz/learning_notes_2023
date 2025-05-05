# epoch ---> a date&time from which a computer measures system time.means computer thinks when time began.consider epoch as a reference point

import time

seconds=time.time()
print("seconds passed since epoch:",seconds)


# ctime() returns epoch time in the form of readable string
# convert=time.ctime(0)
convert=time.ctime(1687601564.879033)
print("convert epoch time to a readable form:",convert)


# sleep() function delay execution according to given time
print("this line print immediately")
time.sleep(2.5)
print("this line print after 2.5 seconds")


# localtime() takes the number of seconds passed since epoch as an argument and returns a tuple containing 9 elements
result=time.localtime(1687601564.879033)
# result=time.localtime()
print(result)


# gmtime takes number of seconds passed since epoch and returns time in UTC
result=time.gmtime(1687601564.879033)
print(result)


# mktime() takes a tuple containing 9 elements and returns the seconds passed since epoch in local time
result=time.mktime(tm_year=2023, tm_mon=6, tm_mday=24, tm_hour=15, tm_min=12, tm_sec=44, tm_wday=5, tm_yday=175, tm_isdst=0)
print(result)