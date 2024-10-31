from django.db import router
from django.urls import path,include
from . import views
from rest_framework import routers

#creation du routeur
router=routers.SimpleRouter()
router.register("allParticipants", views.ParticipantsModelViewSet, basename="participants"),
router.register("organisations", views.OrganisationsModelViewSet, basename="organisations"),
router.register("presses", views.PressesModelViewSet, basename="presses"),

urlpatterns = [
    path('',include(router.urls)),
    path('speakers', views.SpeakersView.as_view(), name='speakers'),
    path('participants', views.ParticipantsSimpleView.as_view(), name="participants"),
    path('etudiants', views.EtudiantsView.as_view(), name="etudiants"),
    path('verifie', views.VerifieView.as_view(), name='verifie'),
    path('confirmation', views.ConfirmationsView.as_view(), name='confirmation'),
    path('rejet', views.RejetsView.as_view(), name='rejet'),
    path('remerciments', views.RemercimentsView.as_view(), name='remerciments'),
    path('inscription', views.InscritsView.as_view(), name='inscription'),
]
