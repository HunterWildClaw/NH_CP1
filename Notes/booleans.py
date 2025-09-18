#NH 2nd Booleans Notes

import time
import datetime as date

over = False

print(over)

name = "Ms. LaRose"

print(bool(name))


current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current Time in seconds since January 1, 1970(epoch time): {current_time}")
print(f"Curent Time: {readable_time}")

now = date.date.today()
hour = now.hour()
# Month = %m ( %b, %B )
# day = %d
# year = %Y, %y
# hour = %H
# minutes = %M
# seconds = %S

print(f"Current time according to datetime: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is a String: {isinstance(current_hour, str)}")
print(f"My hour variable is a Integer: {isinstance(current_hour, int)}")
print(f"My hour variable is a Float: {isinstance(current_hour, float)}")