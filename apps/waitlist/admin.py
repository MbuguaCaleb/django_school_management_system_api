from django.contrib import admin
from .models import WaitlistEntry


class WaitListEntryAdmin(admin.ModelAdmin):
    # the value of list display must be a tuple
    list_display = ('first_name', 'last_name', 'email',
                    'notes', 'created_at', 'updated_at')

    search_fields = ('first_name', )


admin.site.register(WaitlistEntry, WaitListEntryAdmin)
