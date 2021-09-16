
from datetime import date, timedelta
from django.db.models import Max, Avg
from celery.utils.log import get_task_logger

from acmon.celery import app

from apps.car.models import Car
from apps.tracking.models import Record, Trip
from .geotools import get_track_distance

logger = get_task_logger(__name__)

def create_trip(car, first_record, last_record, is_active_trip):
    """Create trip from records"""
    trip_distance = get_track_distance(first_record, last_record)
    trip_records = Record.objects.filter(car=car,
                                         timestamp__lte=last_record.timestamp
                                         )
    max_speed = trip_records.aggregate(Max('speed'))['speed__max']

    if trip_distance > last_record.car.department.insignificant_distance:
        if is_active_trip:
            try:
                last_trip = Trip.objects.filter(car=car).latest()
                trip_records = trip_records.filter(timestamp__gte=last_trip.start_time)
                avg_speed = round(trip_records.aggregate(Avg('speed'))['speed__avg'])

                last_trip.name =  f'{first_record.car.number} {last_trip.start_time} - {last_record.timestamp}'
                last_trip.distance += trip_distance
                last_trip.finish_time = last_record.timestamp
                last_trip.avg_speed = avg_speed
                last_trip.max_speed = max(last_trip.max_speed, max_speed)
                last_trip.save()
                logger.info("Updated trip %s", last_trip)
            except:
                logger.warning("Previous trip does not exist")
                print("Previous trip does not exist")
        else:
            trip_records = trip_records.filter(timestamp__gte=first_record.timestamp)
            avg_speed = round(trip_records.aggregate(Avg('speed'))['speed__avg'])

            trip = Trip.objects.create(name = f'{first_record.car.number} {first_record.timestamp} - {last_record.timestamp}',
                                       car=car,
                                       start_time=first_record.timestamp,
                                       finish_time=last_record.timestamp,
                                       distance = trip_distance,
                                       avg_speed = avg_speed,
                                       max_speed = max_speed,
                                       )
            logger.info("Created trip %s", trip)


@app.task
def create_trips(for_date=None):
    """ Create trips for previous day or for given date """

    if not for_date:
        for_date = date.today() - timedelta(days=1)

    for car in Car.objects.filter(is_active=True):
        is_active_trip = False
        first_record = True
        trip_started = False
        first_record_obj = None
        last_record_obj = None

        for record in Record.objects.filter(car=car,
                                            timestamp__year=for_date.year,
                                            timestamp__month=for_date.month,
                                            timestamp__day=for_date.day
                                            ) \
                                    .order_by('timestamp'):

            # check if trip in progress
            if first_record and not record.is_parked:
                if not record.in_insignificant_distance():
                    is_active_trip = True
                    trip_started = True
                    first_record_obj = record
                first_record = False
                continue

            # check if trip in progress
            if not trip_started:
                trip_started = True
                first_record_obj = record
                continue

            last_record_obj = record

            # check if trip is finished
            if trip_started and record.in_insignificant_distance() and record.is_parked:
                trip_started = False
                create_trip(car, first_record_obj, last_record_obj, is_active_trip)

        # if car is not returned in home location
        if trip_started:
            create_trip(car, first_record_obj, last_record_obj, is_active_trip)
