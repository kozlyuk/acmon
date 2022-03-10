import datetime, calendar
from apps.tracking.tasks import create_trips

year = 2022
months = [1,2,3]
for month in months:
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    for date in days:
        create_trips(date)
