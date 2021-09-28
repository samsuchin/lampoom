from requests.api import get, head
from read.models import ArtWork, Magazine, Work
from ads.models import Ad
from django.shortcuts import render
import requests
from django.conf import settings
from django.db.models import Q, base
from django.contrib.auth import get_user_model
from itertools import chain
from django.core.paginator import Paginator
from .utils import get_user_id
import time
from random import getrandbits
from django.contrib import messages

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

def search(request):
    search = request.GET.get("search", "")
    works = Work.objects.filter(active=True).filter(
    Q(title__icontains=search)|
    Q(writer__first_name__icontains=search)|
    Q(writer__last_name__icontains=search)|
    Q(writer__display_name__icontains=search)|
    Q(custom_display_name__icontains=search)).order_by("-created_at").distinct()

    magazines = Magazine.objects.filter(active=True).filter(
    Q(title__icontains=search)|
    Q(works__title__icontains=search)|
    Q(works__writer__first_name__icontains=search)|
    Q(works__writer__last_name__icontains=search)|
    Q(works__custom_display_name__icontains=search)).order_by("-created_at").distinct()

    users = get_user_model().objects.filter(is_active=True).filter(
        Q(display_name__icontains=search)|
        Q(first_name__icontains=search)|
        Q(last_name__icontains=search)).order_by("-date_joined").distinct()
    qs_chain = chain(works, magazines, users)
    results = sorted(qs_chain, 
                key=lambda instance: instance.pk, 
                reverse=True)
    paginator = Paginator(results, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "results": page_obj,
        "search": search
    }
    get_copy = request.GET.copy()
    if get_copy.get("page"):
        get_copy.pop("page")
    context["get_copy"] = get_copy

    return render(request, "search_results.html", context)

def lottery(request):

    if request.method=="POST":
        username = request.POST.get("twitter_username")
        user_id = get_user_id(username)

        if not user_id:
            messages.error(request, "Please enter a valid username")
            return render(request, "lottery.html")

        base_url = f"https://api.twitter.com/2/users/{user_id}/following?user.fields=id&max_results=1000"
        bearer_token = settings.TWITTER_BEARER_TOKEN
        headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f'Bearer {bearer_token}',
                }
        
        response = requests.get(base_url, headers=headers)
        result_count = int(response.json()["meta"]["result_count"])
        if result_count > 0:
            for user in response.json()["data"]:
                if user["id"] == "28849244":
                    print("FOLLOWS")
                    messages.success(request, "You have been entered in the lottery!")
                    return render(request, "lottery.html")
        print("Does not follow")
        messages.error(request, "You do not follow @harvardlampoon on twitter.")
    
    return render(request, "lottery.html")

def about(request):
    return render(request, "about.html")