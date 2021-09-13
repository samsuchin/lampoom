from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

class Work(models.Model):
    title = models.CharField(max_length=200)
    art_work = models.ForeignKey("ArtWork", null=True, blank=True, on_delete=models.SET_NULL)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    content = HTMLField()
    created_at = models.DateTimeField()
    voice_file = models.FileField(upload_to="voices/", null=True, blank=True)
    active = models.BooleanField(default=True)
    classic = models.BooleanField(default=False)
    custom_display_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_display_name(self):
        if self.custom_display_name:
            return self.custom_display_name
        return self.writer.display_name

class ArtWork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="artwork/")
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    works = models.ManyToManyField(Work, related_name="magazines")
    description = models.TextField(max_length=1000, null=True, blank=True)
    special_link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.CharField(max_length=4)
    seller_link = models.URLField()
    active = models.BooleanField(default=True)
    description = HTMLField()
    cover_image = models.ForeignKey(ArtWork, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title