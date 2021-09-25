from django import template
from ..models import Ad

register = template.Library()


@register.simple_tag
def get_ad(ad_type):
    ad = Ad.objects.filter(ad_type=ad_type, active=True).order_by("?").first()
    return ad