from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("trip", api.TripViewSet)
router.register("record", api.RecordViewSet)

urlpatterns = (
    path("api/", include(router.urls)),
)
