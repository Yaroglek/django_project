from django.contrib import admin
from .models import Image, DemandContent, GeographyContent, SkillsContent


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(DemandContent)
class DemandContentAdmin(admin.ModelAdmin):
    pass


@admin.register(GeographyContent)
class GeographyContentAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillsContent)
class SkillsContentAdmin(admin.ModelAdmin):
    pass
