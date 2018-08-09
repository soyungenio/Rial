from django.contrib import admin
from main.models import *


class SliderMainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SliderMain._meta.fields]

    class Meta:
        model = SliderMain


admin.site.register(SliderMain, SliderMainAdmin)


class Block3MainTextInline(admin.TabularInline):
    model = Block3MainText
    extra = 3


class Block3MainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Block3Main._meta.fields]
    inlines = [Block3MainTextInline]

    class Meta:
        model = Block3Main


admin.site.register(Block3Main, Block3MainAdmin)


class SalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sales._meta.fields]

    class Meta:
        model = Sales


admin.site.register(Sales, SalesAdmin)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Questions._meta.fields]

    class Meta:
        model = Questions


admin.site.register(Questions, QuestionsAdmin)


class ContactsPhonesInline(admin.TabularInline):
    model = ContactsPhones
    extra = 2


class ContactsBusinessInline(admin.TabularInline):
    model = ContactsBusiness
    extra = 2


class SocialsInline(admin.TabularInline):
    model = Socials
    extra = 2


class ContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contacts._meta.fields]
    inlines = [ContactsPhonesInline, ContactsBusinessInline, SocialsInline]

    class Meta:
        model = Contacts


admin.site.register(Contacts, ContactsAdmin)
