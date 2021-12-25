from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _
from .models import ABUser, ABUserTranslation, SocialLink, Skill


class ABUserTranslationInline(admin.StackedInline):
    model = ABUserTranslation
    extra = 0


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class ABUserAdmin(admin.OSMGeoAdmin):
    """ User Model for admin """
    list_display = (
        'email',
        'first_name',
        'last_name',
        'last_login',
        'date_joined',
    )
    fieldsets = (
        (None, {
            'fields': ('email',),
        }),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'avatar',
                'phone',
                'date_of_birth',
                'address',
                'location',
                'about',
                'experience',
            ),
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('last_login', 'date_joined')
    inlines = (ABUserTranslationInline, SocialLinkInline, SkillInline)


admin.site.register(ABUser, ABUserAdmin)
