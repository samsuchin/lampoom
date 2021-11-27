from read.models import ArtWork, Work
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSettingsForm

def account_detail(request, url_username):
    account = get_object_or_404(get_user_model(), url_username=url_username)
    works = Work.objects.filter(active=True).filter(Q(writer=account) | Q(art_work__artist=account)).filter(original_work=True, art_work__original_work=True).distinct().order_by('-created_at')
    context = {
        "account": account,
        "works": works
    }
    return render(request, "account/detail.html", context)

@login_required
def account_settings(request):
    user = request.user
    if request.method=="POST":
        form = UserSettingsForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            use_real_name = request.POST.get("use_real_name")
            user.use_real_name = True if use_real_name == "on" else False
            user.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("account_settings")
    else:
        form = UserSettingsForm(instance=user)
    context = {
        "account": user,
        "form": form
    }
    return render(request, "account/settings.html", context)