from django.contrib import admin
from pages.models import *


class PagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pages._meta.fields]

    class Meta:
        model = Pages


admin.site.register(Pages, PagesAdmin)