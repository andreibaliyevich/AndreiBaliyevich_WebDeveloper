from django.conf import settings
from main.models import ABUser


def main_context(request):
    """ Main context """
    context = {
        'SITE_NAME': settings.SITE_NAME,
        'ABUSER': ABUser.objects.first(),
    }
    return context
