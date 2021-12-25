from os.path import splitext
from django.utils import timezone


def get_user_avatar_path(instance, filename):
    """ Get path of avatar """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1]
    return f'avatars/{ timestamp }{ file_ext }'
