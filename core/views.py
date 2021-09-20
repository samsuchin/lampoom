from read.models import ArtWork, Magazine, Work
from ads.models import Ad
from django.shortcuts import render

# Create your views here.

def index(request):
    works = Work.objects.filter(featured=False, active=True).order_by("?").distinct()[:5]
    featured_works = Work.objects.filter(featured=True, active=True).order_by("?").distinct()[:2]
    magazine = Magazine.objects.filter(featured=True, active=True).order_by("created_at").first()
    context = {
        "featured_works": featured_works,
        "works": works,
        "magazine": magazine
    }
    return render(request, "index.html", context)

