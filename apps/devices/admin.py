from django.contrib import admin

from . import models


class ParameterAdmin(admin.ModelAdmin):
    list_display = [
        "code", "name", "group"
    ]


admin.site.register(models.Parameter, ParameterAdmin)
