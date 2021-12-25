from easy_thumbnails.fields import ThumbnailerImageField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .utilities import get_cover_path, get_thumbnail_path, get_image_path


class Project(models.Model):
    """ Project Model """
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    slug = models.SlugField(max_length=128, unique=True, verbose_name=_('Slug'))

    cover = models.ImageField(upload_to=get_cover_path, verbose_name=_('Cover'))
    thumbnail = ThumbnailerImageField(
        upload_to=get_thumbnail_path,
        resize_source={
            'size': (480, 300),
            'crop': 'smart',
            'autocrop': True,
            'quality': 100,
        },
        verbose_name=_('Thumbnail'),
    )

    description = models.TextField(verbose_name=_('Description'))
    code_url = models.URLField(verbose_name=_('Code URL'))
    project_url = models.URLField(blank=True, verbose_name=_('Project URL'))

    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('End date'),
    )

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', args=[self.slug])

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['-end_date', '-start_date', '-id']


class ProjectTranslation(models.Model):
    """ Project Translation Model """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name=_('Project'),
    )
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES[1:],
        verbose_name=_('Language'),
    )

    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Project Translation')
        verbose_name_plural = _('Project Translations')
        ordering = ['project', 'language']
        unique_together = ['project', 'language']


class ProjectImage(models.Model):
    """ Project Image Model """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name=_('Project'),
    )
    image = models.ImageField(upload_to=get_image_path, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')
        ordering = ['project', 'id']
