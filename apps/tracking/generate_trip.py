import datetime, calendar
year = 2021
month = 9
num_days = calendar.monthrange(year, month)[1]
days = [datetime.date(year, month, day) for day in range(1, num_days+1)]

from apps.tracking.tasks import create_trips

for date in days:
    create_trips(date)
