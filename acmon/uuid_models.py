import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True, editable=False)
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, editable=False)

    class Meta:
        abstract = True
