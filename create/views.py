from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from read.models import Work, ArtWork
from django.core.paginator import Paginator
from ads.models import Ad
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def works(request):
    works = Work.objects.filter(writer=request.user).order_by("created_at")
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "works": page_obj,
        
    }

    if request.method=="POST":
        new_work = Work.objects.create(title=request.POST.get("title"), active=False, writer=request.user)
        return redirect(reverse("manage_work_detail", kwargs={"pk": new_work.pk}))

    return render(request, "create/works.html", context)



class work_detail(UpdateView, LoginRequiredMixin):
    model = Work
    template_name = "create/work_detail.html"
    context_object_name = "work"
    fields = ["title", "art_works", "content", "created_at", "active", "featured", "original_work", "custom_display_name", "voice_file",]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["art_works"] = self.get_object().art_works.all().order_by("order")
        return context

    def get_success_url(self):
        obj = self.object
        return reverse("manage_work_detail", kwargs={"pk": self.get_object().pk})
