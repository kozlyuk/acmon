"""
Custom user model manager for accounts.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.apps import apps


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where mobile_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, mobile_number, email, password=None,
                    is_active=False, is_staff=False, first_name='', last_name=''):
        """
        Creates and saves a User with the given mobile number, email and password.
        """
        if not mobile_number:
            raise ValueError(_('User must have an mobile number'))
        model = apps.get_model(app_label='accounts', model_name='User')
        if email and model.objects.filter(email=self.normalize_email(email)).exists():
            raise ValueError(_("User with such email already exist"))

        user = self.model(
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            is_active=is_active,
            is_staff=is_staff,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, email, password):
        """
        Create and save a SuperUser with the given mobile_number, email and password.
        """
        if not email:
            raise ValueError(_('Superuser must have an email address'))
        user = self.create_user(
            mobile_number=mobile_number,
            email=email,
            password=password,
            is_active=True
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_registered = True
        user.save(using=self._db)
        return user
