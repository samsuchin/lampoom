from django.urls import path
from .views import *

urlpatterns = [
    path("works/", works, name="manage_works"),
    path("works/<pk>/", work_detail.as_view(), name="manage_work_detail"),
]