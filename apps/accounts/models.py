from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from acmon.uuid_models import UUIDModel
from .managers import CustomUserManager


def avatar_directory_path(instance, filename):
    """ file will be uploaded to MEDIA_ROOT/avatars/user_id/<filename> """
    return 'avatars/user_{0}/{1}'.format(instance.pk, filename)


class User(AbstractUser):
    """
    Custom user model where mobile_number is the unique identifiers
    for authentication instead of usernames.
    Added fields mobile_number, birth_date, avatar, theme
    """
    phone_regex = RegexValidator(regex=r'^\d{10}$', message=_("Mobile number must contain 10 digits"))

    LANG_CHOICES = (
        ('en', 'en_us'),
        ('uk', 'uk'),
    )

    username = None
    email = models.EmailField(_('Email address'), unique=True)
    mobile_number = models.CharField(_('Mobile number'), max_length=10, validators=[phone_regex], unique=True)
    lang = models.CharField(_('Interface language'), max_length=2, choices=LANG_CHOICES, default='uk')
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    avatar = models.ImageField(_('Photo'), upload_to=avatar_directory_path, default='avatars/no_image.jpg', blank=True)
    is_registered = models.BooleanField(_('Registered'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# class Operator(models.Model):

#     user = models.OneToOneField(User, verbose_name=_('System user'), on_delete=models.CASCADE)

#     class Meta:
#         pass

#     def __str__(self):
#         return f"{self.last_name} {self.first_name}"


# class Driver(models.Model):

#     # Relationships
#     user = models.OneToOneField(User, verbose_name=_('System user'), on_delete=models.CASCADE)

#     class Meta:
#         pass

#     def __str__(self):
#         return f"{self.last_name} {self.first_name}"
