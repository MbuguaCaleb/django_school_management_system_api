from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_student', 'is_staff', 'is_admin')
    list_filter = ('is_student', 'is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_student', 'is_admin', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class UserProfileAdmin(admin.ModelAdmin):
    pass


# this takes in the models we wish to include in the admin area
# The second parameter ie UserAdmin makes it custom according to how we want
# We do not want to include all the fields by default and thats why we are adding a second option
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
