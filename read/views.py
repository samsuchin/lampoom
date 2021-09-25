from ads.models import Ad
from django.http.response import JsonResponse
from read.models import ArtWork, Magazine, Work
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
import json
from django.db.models.functions import Lower
from django.db.models import Q

def detect(request):
    return render(request, "read/smile_detect.html")

def works(request):
    filter_qs = request.GET.get("filter", "")
    print(filter_qs)
    works = Work.objects.filter(active=True).filter(
    Q(title__icontains=filter_qs)|
    Q(writer__first_name__icontains=filter_qs)|
    Q(writer__last_name__icontains=filter_qs)|
    Q(writer__display_name__icontains=filter_qs)|
    Q(custom_display_name__icontains=filter_qs)).order_by("-created_at").distinct()
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "works": page_obj,
        "filter": filter_qs
    }
    get_copy = request.GET.copy()
    if get_copy.get("page"):
        get_copy.pop("page")
    context["get_copy"] = get_copy

    return render(request, "read/works.html", context)

def work_detail(request, work_pk):
    work = get_object_or_404(Work, pk=work_pk)
    art_works = work.art_works.all().order_by("order")
    context = {
        "work": work,
        "art_works": art_works
    }
    return render(request, "read/work_detail.html", context)

def add_laugh_score(request):
    if request.method=="POST":
        data = json.loads(request.body)
        work_pk = data.get("work_pk")
        work = Work.objects.get(pk=work_pk)
        work.laugh_score+=1
        work.save()
        return JsonResponse({"score": work.laugh_score})

def magazines(request):
    filter_qs = request.GET.get("filter", "")
    magazines = Magazine.objects.filter(active=True).filter(
    Q(title__icontains=filter_qs)|
    Q(works__title__icontains=filter_qs)|
    Q(works__writer__first_name__icontains=filter_qs)|
    Q(works__writer__last_name__icontains=filter_qs)|
    Q(works__custom_display_name__icontains=filter_qs)).order_by("-created_at").distinct()
    paginator = Paginator(magazines, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "magazines": page_obj,
        "filter": filter_qs
    }
    get_copy = request.GET.copy()
    if get_copy.get("page"):
        get_copy.pop("page")
    context["get_copy"] = get_copy
    return render(request, "read/magazines.html", context)

def magazine_detail(request, magazine_pk):
    magazine = get_object_or_404(Magazine, pk=magazine_pk)
    context = {
        "magazine": magazine
    }
    return render(request, "read/magazine_detail.html", context)
