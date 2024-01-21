from django.db import models


class DemandContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    graphic = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.title


class GeographyContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    graphic = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.title


class SkillsContent(models.Model):
    title = models.CharField(max_length=50)
    load_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SkillsYear(models.Model):
    title = models.CharField(max_length=20)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    graphic = models.ImageField(upload_to="images/skills", null=True)
    skills_content = models.ForeignKey(SkillsContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
