from geopy import distance
from django.conf import settings


def get_distance_between_points(location1, location2):
    return distance.geodesic(location1, location2).km


def get_track_distance(record1, record2):
    odo1 = record1.io_elements.get('16')
    odo2 = record2.io_elements.get('16')
    if odo1 and odo2:
        return abs(odo2 - odo1) / 1000
