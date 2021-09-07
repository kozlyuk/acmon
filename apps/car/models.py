from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from colorfield.fields import ColorField

from acmon.uuid_models import UUIDModel


class Company(UUIDModel):

    # Fields
    name = models.CharField(_('Name'), max_length=45)
    contact_person = models.CharField(_('Contact person'), max_length=45, blank=True, null=True)
    contact_phone = models.CharField(_('Contact phone'), max_length=30, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return str(self.name)


class Department(UUIDModel):

    # Relationships
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))

    # Fields
    name = models.CharField(max_length=45)
    base_latitude = models.PositiveIntegerField('Base latitude', default=0, validators=[MaxValueValidator(900000000)])
    base_longitude = models.PositiveIntegerField('Base longitude', default=0, validators=[MaxValueValidator(900000000)])
    insignificant_distance = models.FloatField('Insignificant distance', default=10)
    around_distance = models.FloatField('Around distance', default=0.1)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return str(self.name)


class Brand(UUIDModel):

    # Fields
    name = models.CharField(_('Name'), max_length=30)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return str(self.name)


class Model(UUIDModel):

    # Relationships
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_('Brand'))

    # Fields
    name = models.CharField(_('Name'), max_length=30)
    year_of_production = models.PositiveSmallIntegerField('Year of production', blank=True, null=True)

    class Meta:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

    def __str__(self):
        return f'{self.name} {self.year_of_production}'


class Car(UUIDModel):

    # Relationships
    model = models.ForeignKey(Model, on_delete=models.PROTECT, verbose_name='Model')
    department = models.ForeignKey("car.Department", on_delete=models.CASCADE, verbose_name=_('Department'))

    # Fields
    sim_imei = models.CharField(_('Tracker IMEI'), max_length=30)
    sim_number = models.CharField(_('Tracker sim number'), max_length=13)
    number = models.CharField(_('Car number'), max_length=8)
    color = ColorField(_('Car color'), default='#FF0000')
    track_color = ColorField(_('Route color'), default='#0000FF')
    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return str(self.number)
