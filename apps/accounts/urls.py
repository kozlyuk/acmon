from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("Contact", api.ContactViewSet)
# router.register("Operator", api.OperatorViewSet)
# router.register("Driver", api.DriverViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
)
