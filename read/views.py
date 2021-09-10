from read.models import Work
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

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