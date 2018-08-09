from django.contrib import admin
from projects.models import *


class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    extra = 3


class ProjectsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Projects._meta.fields]
    inlines = [ProjectImagesInline]

    class Meta:
        model = Projects


admin.site.register(Projects, ProjectsAdmin)


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectType._meta.fields]

    class Meta:
        model = ProjectType


admin.site.register(ProjectType, ProjectTypeAdmin)


