from django.urls import path
from .views import *

urlpatterns = [
    path("works/", works, name="manage_works"),
    path("works/<pk>/", work_detail.as_view(), name="manage_work_detail"),
    path("artworks/", art_works, name="manage_artworks"),
    path("artworks/<pk>/", art_work_detail.as_view(), name="manage_artwork_detail"),
    path("ads/", ads, name="manage_ads"),
    path("ads/<pk>/", ad_detail.as_view(), name="manage_ad_detail"),
]