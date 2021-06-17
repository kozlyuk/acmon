from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("brand", api.BrandViewSet)
router.register("car", api.CarViewSet, basename="Car")
router.register("company", api.CompanyViewSet)
router.register("department", api.DepartmentViewSet)
router.register("model", api.ModelViewSet)

urlpatterns = (
    path("api/", include(router.urls)),
)
