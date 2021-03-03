from django.contrib import admin
from .models import Certificate


class CertficateAdmin(admin.ModelAdmin):
    # the value of list display must be a tuple
    list_display = ('name', 'created_at', 'updated_at')

    search_fields = ('name', )


admin.site.register(Certificate, CertficateAdmin)
