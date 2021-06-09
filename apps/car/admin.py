from django.contrib import admin

from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class CarAdmin(admin.ModelAdmin):
    list_display = [
        "number",
        "sim_number",
        "sim_imei",
    ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "contact_person",
        "email",
        "contact_phone",
    ]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class ModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Model, ModelAdmin)
