from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
# router.register("Trip", api.TripViewSet)
router.register("Record", api.RecordViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
)
