from ads import ADS
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from read.models import Work, ArtWork
from django.core.paginator import Paginator
from ads.models import Ad
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

@login_required
def works(request):
    works = Work.objects.filter(writer=request.user).order_by("-created_at")
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "works": page_obj,
        
    }

    if request.method=="POST":
        new_work = Work.objects.create(title=request.POST.get("title"), active=False, writer=request.user, created_at=timezone.now())
        return redirect(reverse("manage_work_detail", kwargs={"pk": new_work.pk}))

    return render(request, "create/works.html", context)


class work_detail(UpdateView, LoginRequiredMixin):
    model = Work
    template_name = "create/work_detail.html"
    context_object_name = "work"
    fields = ["title", "art_work", "magazine", "content", "created_at", "featured", "original_work", "custom_display_name", "voice_file",]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        obj = self.object
        return reverse("manage_work_detail", kwargs={"pk": self.get_object().pk})

@login_required
def art_works(request):
    art_works = ArtWork.objects.filter(artist=request.user).order_by("created_at")
    paginator = Paginator(art_works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "art_works": page_obj,
    }

    if request.method=="POST":
        new_artwork = ArtWork.objects.create(title=request.POST.get("title"),  artist=request.user, image=request.FILES.get("image"))
        return redirect(reverse("manage_artwork_detail", kwargs={"pk": new_artwork.pk}))

    return render(request, "create/artworks.html", context)

class art_work_detail(UpdateView, LoginRequiredMixin):
    model = ArtWork
    template_name = "create/artwork_detail.html"
    context_object_name = "art"
    fields = ["title", "image", "order","original_work", "custom_display_name"]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        obj = self.object
        return reverse("manage_artwork_detail", kwargs={"pk": self.get_object().pk})

@login_required
def ads(request):
    ads = Ad.objects.filter(created_by=request.user).order_by("created_at")
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "ads": page_obj,
        "ad_types": ADS.AD_TYPES
        
    }

    if request.method=="POST":
        new_ad = Ad.objects.create(title=request.POST.get("title"), active=True, image=request.FILES.get("image"), ad_type=request.POST.get("ad_type"), created_by=request.user, url=request.POST.get("url"))
        return redirect(reverse("manage_ad_detail", kwargs={"pk": new_ad.pk}))

    return render(request, "create/ads.html", context)


class ad_detail(UpdateView, LoginRequiredMixin):
    model = Ad
    template_name = "create/ad_detail.html"
    context_object_name = "ad"
    fields = ["title", "image",  "ad_type", "url", "active"]

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        obj = self.object
        return reverse("manage_ad_detail", kwargs={"pk": self.get_object().pk})