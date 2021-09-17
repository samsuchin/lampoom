from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

class Work(models.Model):
    title = models.CharField(max_length=200)
    art_works = models.ManyToManyField("ArtWork", related_name="works")
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    content = HTMLField()
    created_at = models.DateTimeField()
    voice_file = models.FileField(upload_to="voices/", null=True, blank=True)
    active = models.BooleanField(default=True)
    classic = models.BooleanField(default=False)
    custom_display_name = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)
    laugh_score = models.PositiveBigIntegerField(default=0)
    original_work = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_display_name(self):
        if self.custom_display_name:
            return self.custom_display_name
        return self.writer.display_name
    
    def get_preview_image(self):
        return self.art_works.all().order_by("order").first()

class ArtWork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="artwork/")
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    custom_display_name = models.CharField(max_length=200, null=True, blank=True)
    original_work = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_display_name(self):
        if self.custom_display_name:
            return self.custom_display_name
        return self.artist.display_name
        

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    works = models.ManyToManyField(Work, related_name="magazines")
    description = HTMLField(null=True, blank=True)
    special_link = models.URLField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    cover_image = models.ForeignKey(ArtWork, null=True, blank=True, on_delete=models.SET_NULL)

    issue_editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="issue_editor")
    art_editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="art_editor")
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title

    def get_total_laughs(self):
        total = 0
        for work in self.works.all():
            total+=work.laugh_score
        return total

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.CharField(max_length=4)
    seller_link = models.URLField()
    active = models.BooleanField(default=True)
    description = HTMLField()
    cover_image = models.ForeignKey(ArtWork, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title