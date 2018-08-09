from django.contrib import admin
from about.models import *


class AdvantagesAdminBullets(admin.TabularInline):
    model = AdvantagesBullets
    extra = 3


class AdvantagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Advantages._meta.fields]
    inlines = [AdvantagesAdminBullets]

    class Meta:
        model = Advantages


admin.site.register(Advantages, AdvantagesAdmin)


class HowWeDoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HowWeDo._meta.fields]

    class Meta:
        model = HowWeDo


admin.site.register(HowWeDo, HowWeDoAdmin)


class StuffBulletsAdmin(admin.TabularInline):
    model = StuffBullets
    extra = 3


class StuffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stuff._meta.fields]
    inlines = [StuffBulletsAdmin]

    class Meta:
        model = Stuff


admin.site.register(Stuff, StuffAdmin)


class ToolsBulletsAdmin(admin.TabularInline):
    model = ToolsBullets
    extra = 3


class ToolsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tools._meta.fields]
    inlines = [ToolsBulletsAdmin]

    class Meta:
        model = Tools


admin.site.register(Tools, ToolsAdmin)


class RepliesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Replies._meta.fields]

    class Meta:
        model = Replies


admin.site.register(Replies, RepliesAdmin)


class PartnersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Partners._meta.fields]

    class Meta:
        model = Partners


admin.site.register(Partners, PartnersAdmin)