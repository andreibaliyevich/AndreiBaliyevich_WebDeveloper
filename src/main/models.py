from easy_thumbnails.fields import ThumbnailerImageField
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MaxValueValidator, RegexValidator
from django.utils import timezone
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from main.model_fields import TranslatedField
from .managers import ABUserManager
from .utilities import get_user_avatar_path


class ABUser(AbstractBaseUser, PermissionsMixin):
    """ User Model """
    email = models.EmailField(unique=True, verbose_name=_('Email'))

    first_name = models.CharField(
        blank=True,
        max_length=150,
        verbose_name=_('First name'),
    )
    last_name = models.CharField(
        blank=True,
        max_length=150,
        verbose_name=_('Last name'),
    )
    translated_first_name = TranslatedField('first_name')
    translated_last_name = TranslatedField('last_name')

    avatar = ThumbnailerImageField(
        default='avatars/default.png',
        upload_to=get_user_avatar_path,
        resize_source={
            'size': (800, 800),
            'crop': 'smart',
            'autocrop': True,
            'quality': 100,
        },
        verbose_name=_('Avatar'),
    )
    phone = models.CharField(
        blank=True,
        max_length=21,
        validators=[
            RegexValidator(
                regex=r'^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){9,16}(\s*)?$',
                message=_('Wrong format!'),
            ),
        ],
        verbose_name=_('Phone'),
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Date of Birth'),
    )

    address = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Address'),
    )
    translated_address = TranslatedField('address')
    location = models.PointField(
        default=Point(0.0, 0.0),
        verbose_name=_('Location'),
    )

    about = models.TextField(blank=True, verbose_name=_('About'))
    translated_about = TranslatedField('about')
    
    experience = models.TextField(blank=True, verbose_name=_('Experience'))
    translated_experience = TranslatedField('experience')

    is_active = models.BooleanField(default=False, verbose_name=_('Active'))
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Staff status'),
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_('Superuser status'),
    )

    last_login = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Last login'),
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Date joined'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ABUserManager()

    def get_age(self):
        return (
            timezone.now().year
            - self.date_of_birth.year
            - int(
                (timezone.now().month, timezone.now().day) < (
                    self.date_of_birth.month, self.date_of_birth.day)))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['email']


class ABUserTranslation(models.Model):
    """ ABUser Translation Model """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('User'),
    )
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES[1:],
        verbose_name=_('Language'),
    )

    first_name = models.CharField(max_length=150, verbose_name=_('First name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last name'))

    address = models.CharField(max_length=255, verbose_name=_('Address'))

    about = models.TextField(verbose_name=_('About'))
    experience = models.TextField(verbose_name=_('Experience'))

    class Meta:
        verbose_name = _('ABUser Translation')
        verbose_name_plural = _('ABUser Translations')
        ordering = ['user', 'language']
        unique_together = ['user', 'language']


class SocialLink(models.Model):
    """ Social Link Model """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )

    icon_name = models.CharField(
        max_length=24,
        verbose_name=_('Name of icon'),
    )
    link_url = models.URLField(verbose_name=_('URL of Link'))

    position = models.PositiveSmallIntegerField(
        db_index=True,
        verbose_name=_('Position'),
    )

    class Meta:
        verbose_name = _('Social Link')
        verbose_name_plural = _('Social Links')
        ordering = ['user', 'position']
        unique_together = ['user', 'position']


class Skill(models.Model):
    """ Skill Model """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )

    name = models.CharField(max_length=64, verbose_name=_('Name'))
    progress = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
        ],
        verbose_name=_('Progress'),
    )

    position = models.PositiveSmallIntegerField(
        db_index=True,
        verbose_name=_('Position'),
    )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
        ordering = ['user', 'position']
        unique_together = ['user', 'position']
