from django.contrib import admin
from .models import Project, ProjectTranslation, ProjectImage


class ProjectTranslationInline(admin.TabularInline):
    model = ProjectTranslation
    extra = 0


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    """ Project Model for admin """
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ProjectTranslationInline, ProjectImageInline)


admin.site.register(Project, ProjectAdmin)
