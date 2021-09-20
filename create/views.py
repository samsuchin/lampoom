from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required
from read.models import Work, ArtWork
from django.core.paginator import Paginator
from ads.models import Ad
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def articles(request):
    works = Work.objects.filter(writer=request.user).order_by("created_at")
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "works": page_obj,
        
    }
    return render(request, "create/articles.html", context)



class article_detail(UpdateView, LoginRequiredMixin):
    model = Work
    template_name = "create/article_detail.html"
    context_object_name = "article"
    fields = ["title", "art_works", "content", "active"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["art_works"] = self.get_object().art_works.all().order_by("order")
        return context

    def get_success_url(self):
        obj = self.object
        return reverse("manage_article_detail", kwargs={"pk": self.get_object().pk})
