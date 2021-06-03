from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("Brand", api.BrandViewSet)
router.register("Car", api.CarViewSet)
router.register("Company", api.CompanyViewSet)
router.register("Department", api.DepartmentViewSet)
router.register("Model", api.ModelViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
)
