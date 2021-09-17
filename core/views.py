from read.models import ArtWork, Magazine, Work
from django.shortcuts import render

# Create your views here.

def index(request):
    works = Work.objects.filter(featured=False).order_by("?").distinct()[:6]
    featured_works = Work.objects.filter(featured=True).order_by("?").distinct()[:2]
    magazine = Magazine.objects.filter(featured=True).first()
    context = {
        "featured_works": featured_works,
        "works": works,
        "magazine": magazine
    }
    return render(request, "index.html", context)