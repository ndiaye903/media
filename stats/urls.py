from django.db import router
from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.SimpleRouter()

urlpatterns = [
    path('',include(router.urls)),
    path("stats", views.StatsView.as_view(), name="stats"),
]
