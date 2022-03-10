from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("trip", api.TripViewSet, basename='Trip')
router.register("record", api.RecordViewSet, basename='Record')

urlpatterns = (
    path("", include(router.urls)),
)
