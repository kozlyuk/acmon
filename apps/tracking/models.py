from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from acmon.uuid_models import UUIDModel


class Trip(UUIDModel):

    # Relationships
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, verbose_name=_('Car'))
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Driver'),
                               blank=True, null=True, on_delete=models.SET_NULL)

    # Fields
    start_time = models.DateTimeField(_('Start time'))
    finsh_time = models.DateTimeField(_('Finish time'))

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')

    def __str__(self):
        return f'{self.car.number} - {self.start_time} - {self.finsh_time}'


class Record(UUIDModel):

    # Relationships
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, verbose_name=_('Car'))

    # Fields
    timestamp = models.DateTimeField('Timestamp')
    priority = models.PositiveIntegerField('Priority', default=0, validators=[MaxValueValidator(2)])
    longitude = models.PositiveIntegerField('Longitude', validators=[MaxValueValidator(900000000)])
    latitude = models.PositiveIntegerField('Latitude', validators=[MaxValueValidator(900000000)])
    altitude = models.PositiveSmallIntegerField('Altitude')
    angle = models.PositiveSmallIntegerField('Angle', default=0, validators=[MaxValueValidator(360)])
    satellites = models.PositiveSmallIntegerField('Satelites', default=0)
    speed = models.PositiveSmallIntegerField('Speed', default=0)
    event_id = models.PositiveSmallIntegerField('Event ID', default=0)
    io_elements = models.JSONField('IO Elements', default=list)

    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return str(self.timestamp)
