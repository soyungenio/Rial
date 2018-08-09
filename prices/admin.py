from django.contrib import admin
from prices.models import *


class PricesForkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PricesFork._meta.fields]

    class Meta:
        model = PricesFork


admin.site.register(PricesFork, PricesForkAdmin)


class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlaceType._meta.fields]

    class Meta:
        model = PlaceType


admin.site.register(PlaceType, PlaceTypeAdmin)


class ServicesCategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServicesCategories._meta.fields]

    class Meta:
        model = ServicesCategories


admin.site.register(ServicesCategories, ServicesCategoriesAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Services._meta.fields]
    list_display.insert(2, 'get_remonttypes')
    filter_horizontal = ('remonttype',)
    class Meta:
        model = Services


admin.site.register(Services, ServicesAdmin)


class ServicesSubcategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServicesSubcategories._meta.fields]

    class Meta:
        model = ServicesSubcategories


admin.site.register(ServicesSubcategories, ServicesSubcategoriesAdmin)