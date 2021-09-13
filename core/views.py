from read.models import ArtWork
from django.shortcuts import render

# Create your views here.

def index(request):
    images = ArtWork.objects.all().order_by("?")[:3]
    context = {
        "images": images
    }
    return render(request, "index.html", context)