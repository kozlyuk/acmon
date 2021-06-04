from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _

from acmon.uuid_models import UUIDModel


class Trip(UUIDModel):

    # Relationships
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, verbose_name=_('Car'))

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
    department = models.ForeignKey("car.Department", on_delete=models.CASCADE, verbose_name=_('Department'))

    # Fields
    timestamp = models.DateTimeField('Timestamp')
    priority = models.PositiveIntegerField('Priority', default=0, validators=[MaxValueValidator(2)])
    longitude = models.PositiveIntegerField('Longitude', validators=[MaxValueValidator(900000000)])
    latitude = models.PositiveIntegerField('Latitude', validators=[MaxValueValidator(900000000)])
    altitude = models.PositiveSmallIntegerField('Altitude')
    angle = models.PositiveIntegerField('Angle', default=0, validators=[MaxValueValidator(360)])
    satellites = models.PositiveSmallIntegerField('Satelites')
    speed = models.PositiveSmallIntegerField('Speed', default=0)
    request_data = models.BinaryField('Request data', blank=True, null=True)

    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return str(self.timestamp)
