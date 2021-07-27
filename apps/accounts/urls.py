from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register("contact", api.ContactViewSet)

urlpatterns = (
    path("api/", include(router.urls)),
    path("api/register/", api.Register.as_view(), name='register'),
    path("api/activate_email/<str:uidb64>/<str:token>/", api.ActivateEmail.as_view(), name='activate_email'),
    path("api/v1/activate_sms/<str:mobile_number>/<str:otp>/", api.ActivateSMS.as_view(), name='activate_sms'),
)
