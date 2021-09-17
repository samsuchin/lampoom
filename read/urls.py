from django.urls import path
from .views import *

urlpatterns = [
    path("test", detect, name="detect"),
    path("works/", works, name="works"),
    path("works/<work_pk>/", work_detail, name="work_detail"),
    path("magazines/", magazines, name="magazines"),
    path("magazines/<magazine_pk>/", magazine_detail, name="magazine_detail"),
    path("work/add-laugh-score/", add_laugh_score, name="add_laugh_score")
]