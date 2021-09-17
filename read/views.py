from django.http.response import JsonResponse
from read.models import Magazine, Work
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
import json

def detect(request):
    return render(request, "read/smile_detect.html")

def works(request):
    works = Work.objects.filter(active=True).order_by("-created_at")
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "works": page_obj
    }
    return render(request, "read/works.html", context)

def work_detail(request, work_pk):
    work = get_object_or_404(Work, pk=work_pk)
    context = {
        "work": work
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
    magazines = Magazine.objects.filter(active=True).order_by("-created_at")
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "magazines": page_obj
    }
    return render(request, "read/magazines.html", context)

def magazine_detail(request, magazine_pk):
    magazine = get_object_or_404(Magazine, pk=magazine_pk)
    context = {
        "magazine": magazine
    }
    return render(request, "read/magazine_detail.html", context)
