from django.urls import path
from .views import *

urlpatterns = [
    path("articles/", articles, name="manage_articles"),
    path("articles/<pk>/", article_detail.as_view(), name="manage_article_detail"),
]