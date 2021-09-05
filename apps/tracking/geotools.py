from geopy import distance
from django.conf import settings


def get_home_location():
    return (settings.BASE_LATITUDE, settings.BASE_LONGITUDE)


def get_distance_from_home(location):
    return distance.geodesic(get_home_location(), location).km


def get_distance_between_records(location1, location2):
    return distance.geodesic(location1, location2).km


def get_track_distance(record1, record2):
    odo1 = record1.io_elements.get('16')
    odo2 = record2.io_elements.get('16')
    if odo1 and odo2:
        return abs(odo2 - odo1)
