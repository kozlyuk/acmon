from django.contrib import admin
from django import forms

from . import models


class TripAdmin(admin.ModelAdmin):
    list_display = [
        "car",
        "start_time",
    ]


class RecordAdmin(admin.ModelAdmin):
    list_display = [
        "timestamp",
        "car",
        "event_id",
        "longitude",
        "latitude",
        "is_parked",
    ]


admin.site.register(models.Trip, TripAdmin)
admin.site.register(models.Record, RecordAdmin)
