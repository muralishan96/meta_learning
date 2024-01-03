import sys 
location = sys.path
for i in location:
    print(i)

import calendar
leapdays = calendar.leapdays(2000,2022)
print(leapdays)
leap = calendar.isleap(2022)
print(leap)

