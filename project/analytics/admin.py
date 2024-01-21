from django.contrib import admin
from .models import *


@admin.register(DemandContent)
class DemandContentAdmin(admin.ModelAdmin):
    pass


@admin.register(GeographyContent)
class GeographyContentAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillsContent)
class SkillsContentAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillsYear)
class SkillsYearAdmin(admin.ModelAdmin):
    pass
