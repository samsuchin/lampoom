from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('display_name','first_name','last_name', 'email', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Information', {'fields': ('display_name', 'email', 'password', 'date_joined', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Misc', {'fields': ('first_name', 'last_name','graduation_year', 'board', 'profile_picture', 'profile_picture_preview')}),
        
    )
    readonly_fields = ['date_joined', 'profile_picture_preview']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email', 'display_name', 'first_name', 'last_name')
    ordering = ('pk',)

admin.site.register(User, CustomUserAdmin)


app_models = apps.get_app_config('account').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
