from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from apps.tracking.geotools import get_distance_between_points

from acmon.uuid_models import UUIDModel


class Trip(UUIDModel):

    # Relationships
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, verbose_name=_('Car'))
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Driver'),
                               blank=True, null=True, on_delete=models.SET_NULL)

    # Fields
    name = models.CharField(_('Name'), max_length=100, blank=True, null=True)
    distance = models.FloatField('Distance')
    start_time = models.DateTimeField(_('Start time'))
    finish_time = models.DateTimeField(_('Finish time'))

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')
        get_latest_by = 'finish_time'

    def __str__(self):
        return self.name


class Record(UUIDModel):

    # Relationships
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, verbose_name=_('Car'))

    # Fields
    timestamp = models.DateTimeField('Timestamp')
    priority = models.PositiveIntegerField('Priority', default=0, validators=[MaxValueValidator(2)])
    latitude = models.PositiveIntegerField('Latitude', validators=[MaxValueValidator(900000000)])
    longitude = models.PositiveIntegerField('Longitude', validators=[MaxValueValidator(900000000)])
    altitude = models.PositiveSmallIntegerField('Altitude')
    angle = models.PositiveSmallIntegerField('Angle', default=0, validators=[MaxValueValidator(360)])
    satellites = models.PositiveSmallIntegerField('Satelites', default=0)
    speed = models.PositiveSmallIntegerField('Speed', default=0)
    event_id = models.PositiveSmallIntegerField('Event ID', default=0)
    io_elements = models.JSONField('IO Elements', default=dict, blank=True, null=True)
    is_parked = models.BooleanField(_('Is parked'), default=False)

    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')
        get_latest_by = 'timestamp'

    def __str__(self):
        return str(self.timestamp)

    def set_is_parked(self):
        is_ignition_on = self.io_elements.get('239', True)
        is_movement = self.io_elements.get('240', True)
        if not is_ignition_on and not is_movement:
            self.is_parked = True
            self.save()

    def get_location(self):
        return (self.latitude / 10000000, self.longitude / 10000000)

    def get_base_location(self):
        return (self.car.department.base_latitude / 10000000, self.car.department.base_longitude / 10000000)

    def distance_from_home(self):
        return int(get_distance_between_points(self.get_base_location(), self.get_location()))
    distance_from_home.short_description = "Distance from home, km"

    def in_insignificant_distance(self):
        return self.distance_from_home() <= self.car.department.insignificant_distance
    distance_from_home.short_description = "In insignifacant distance"

    def in_around_distance(self):
        return self.distance_from_home() <= self.car.department.around_distance
    distance_from_home.short_description = "In around distance"
