from django.db import models
from django.utils.translation import ugettext_lazy as _

class Parameter(models.Model):

    # Fields
    code = models.PositiveSmallIntegerField(_('Code'), unique=True)
    name = models.CharField(_('Property Name'), max_length=64)
    bytes = models.PositiveSmallIntegerField(_('Bytes'), null=True, blank=True)
    type = models.CharField(_('Type'), max_length=16)
    min_value = models.IntegerField(_('Minimal Value'), null=True, blank=True)
    max_value = models.IntegerField(_('Maximal Value'), null=True, blank=True)
    multiplier = models.DecimalField(_('Multiplier'), max_digits=8, decimal_places=3, null=True, blank=True)
    units = models.CharField(_('Units'), max_length=16, null=True, blank=True)
    description = models.TextField(_('Description'))
    hw_support = models.TextField(_('Hardware Support'))
    group = models.CharField(_('Parameter Group'), max_length=64)

    class Meta:
        verbose_name = _('Parameter')
        verbose_name_plural = _('Parameters')

    def __str__(self):
        return f'{self.code} - {self.name}'
