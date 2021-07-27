import pyotp
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from rest_framework import viewsets, views, status, permissions
from rest_framework.response import Response

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer
from apps.accounts.services import account_activation_token
from apps.messaging.tasks import send_email, send_sms

from . import serializers
from . import models



class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet for the Contact class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Register(views.APIView):
    """
    Check if resident mobile number exists in DB.
    If post_data valid - updates user data and
    sends confirmation email with token and sms with otp.
    If resident don`t exists return status HTTP_404_NOT_FOUND.
    If post_data not valid return status HTTP_400_BAD_REQUEST.
    If user data  updated return status HTTP_200_OK.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.none()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # check if serializer is valid
        if serializer.is_valid():
            user = serializer.save()
            # send activation email with token
            if settings.EMAIL_ENABLED:
                mail_subject = _('Activate your ACMon account.')
                domain = settings.FRONT_SITE_URL
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)
                message = render_to_string('email/account_activation_email.txt', {
                    'first_name': user.first_name,
                    'account_activation_url': f"{domain}/registration/{uid}/{token}/",
                })
                send_email(mail_subject, message, to=[user.email]) # TODO add delay
            # send activation sms with otp
            if settings.SMS_ENABLED:
                hotp = pyotp.HOTP(settings.OTP_SECRET)
                mobile_number_international = '38' + user.mobile_number
                otp = hotp.at(user.pk)
                send_sms([mobile_number_international], otp) # TODO add delay
            message = _('User registered. Please activate your account from email link or enter OTP code from sms:')
            return Response(message, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateEmail(views.APIView):
    """
    Check actvation url and makes user active.
    If token is valid send HTTP_200_OK and make user active.
    If token is not valid send HTTP_400_BAD_REQUEST.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.none()

    def get(self, request, uidb64, token):
        # check if number is valid
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_registered = True
            user.is_active = True
            user.save()
            return Response(_('Thank you for your email confirmation. Now you can login your account.'),
                            status=status.HTTP_200_OK)
        return Response(_('Activation link is invalid!'),
                        status=status.HTTP_400_BAD_REQUEST)


class ActivateSMS(views.APIView):
    """
    Check actvation url and makes user active.
    If token is valid send HTTP_200_OK and make user active.
    If token is not valid send HTTP_400_BAD_REQUEST.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.none()

    def get(self, request, mobile_number, otp):
        # check if otp code is valid
        try:
            user = User.objects.get(mobile_number=mobile_number)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        hotp = pyotp.HOTP(settings.OTP_SECRET)
        if user is not None and hotp.verify(otp, user.pk):
            user.is_registered = True
            user.is_active = True
            user.save()
            return Response(_('Thank you for your otp confirmation. Now you can login your account.'),
                            status=status.HTTP_200_OK)
        return Response(_('OTP code is invalid!'),
                        status=status.HTTP_400_BAD_REQUEST)
