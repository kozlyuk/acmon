from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("contact", api.ContactViewSet)

urlpatterns = (
    path("", include(router.urls)),
    path("register/", api.Register.as_view(), name='register'),
    path("activate_email/<str:uidb64>/<str:token>/", api.ActivateEmail.as_view(), name='activate_email'),
    path("activate_sms/<str:mobile_number>/<str:otp>/", api.ActivateSMS.as_view(), name='activate_sms'),
)
