from django.contrib import admin
from menu.models import *


class MenuBulletAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MenuBullet._meta.fields]

    class Meta:
        model = MenuBullet


admin.site.register(MenuBullet, MenuBulletAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.fields]

    class Meta:
        model = Page


admin.site.register(Page, PageAdmin)


class Page2Admin(admin.ModelAdmin):
    list_display = [field.name for field in Page2._meta.fields]

    class Meta:
        model = Page2


admin.site.register(Page2, Page2Admin)
