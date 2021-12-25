from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    """ Message Model """
    name = models.CharField(max_length=250, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))

    content = models.TextField(verbose_name=_('Content'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ['-created_at', '-id']
