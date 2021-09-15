from django.urls import path
from .views import *

urlpatterns = [
    path("test", detect, name="detect"),
    path("", works, name="works"),
    path("<work_pk>/", work_detail, name="work_detail"),
    path("work/add-laugh-score/", add_laugh_score, name="add_laugh_score")
]