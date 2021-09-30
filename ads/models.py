from django.db import models
from django.conf import settings
from . import ADS

class Ad(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    image = models.ImageField(upload_to="ads/")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)

    ad_type = models.CharField(choices=ADS.AD_TYPES, max_length=50)
    
    def __str__(self) -> str:
        return f"{self.title} {self.get_ad_type_display()}"
