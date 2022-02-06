from os.path import splitext
from django.utils import timezone


def get_cover_path(instance, filename):
    """ Get path of cover """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1].lower()
    return f'covers/{ timestamp }{ file_ext }'


def get_thumbnail_path(instance, filename):
    """ Get path of thumbnail """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1].lower()
    return f'thumbnails/{ timestamp }{ file_ext }'


def get_image_path(instance, filename):
    """ Get path of image """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1].lower()
    return f'images/{ timestamp }{ file_ext }'
