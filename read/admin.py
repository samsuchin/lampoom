from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from read.models import Work


class WorkAdmin(admin.ModelAdmin):
    model = Work
    ordering = ['-pk']
    search_fields = ['title', 'magazine__title', 'writer__display_name']
    list_display = ["title", "magazine", "writer", "active"]
    list_editable = ["active"]

admin.site.register(Work, WorkAdmin)

app_models = apps.get_app_config('read').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
