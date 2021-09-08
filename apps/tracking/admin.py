from django.contrib import admin
from django import forms

from . import models


class TripAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "distance",
        "start_time",
        "finish_time",
    ]
    ordering = ['-start_time']


class RecordAdmin(admin.ModelAdmin):
    list_display = [
        "timestamp",
        "car",
        "event_id",
        "latitude",
        "longitude",
        "is_parked",
        "distance_from_home"
    ]
    list_filter = ('car__number', 'is_parked', 'event_id', 'priority',)
    ordering = ['-timestamp']


admin.site.register(models.Trip, TripAdmin)
admin.site.register(models.Record, RecordAdmin)
