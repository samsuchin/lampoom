from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path("@<url_username>", account_detail, name="account_detail"),
    path("account/settings/", account_settings, name="account_settings"),
    path('account/', include('django.contrib.auth.urls')),
    path("account/login/", auth_views.LoginView.as_view(form_class=LoginForm)),
]