from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    load_dttm = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


class DemandContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.title


class GeographyContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.title


class SkillsContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.JSONField(null=True)
    load_dttm = models.DateTimeField(auto_now_add=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.title
