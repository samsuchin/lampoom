from read.models import ArtWork, Work
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q

def account_detail(request, url_username):
    account = get_object_or_404(get_user_model(), url_username=url_username)
    works = Work.objects.filter(active=True).filter(Q(writer=account) | Q(art_works__artist=account)).filter(original_work=True, art_works__original_work=True).distinct().order_by('-created_at')
    context = {
        "account": account,
        "works": works
    }
    return render(request, "account/detail.html", context)