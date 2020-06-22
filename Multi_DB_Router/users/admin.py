"""Users Admin section."""

from django.contrib import admin
from. models import CustomUser


class CustomerAdmin(admin.ModelAdmin):
    """Customer Admin section."""

    list_display = ['email', "first_name", 'database']


admin.site.register(CustomUser, CustomerAdmin)
