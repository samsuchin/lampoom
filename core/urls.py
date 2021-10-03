from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("lottery/", lottery, name="lottery"),
    path("search/", search, name="search"),
    path("about/", about, name="about"),
    path("masthead/", masthead, name="masthead"),
    path("comp/", comp, name="comp"),
    path("contact/", contact, name="contact"),
    path("features/", features, name="features"),
]