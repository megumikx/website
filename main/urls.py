
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("obertos/", views.obertos, name="obertos"),
    path("well/", views.well, name="well"),
    path("djin/", views.djin, name="djin"),
    path("about/", views.about, name="about"),
    path("puxliykrolik/", views.puxliykrolik, name="puxliykrolik"),
    path("boombubble/", views.boombubble, name="boombubble"),
    path("chokki/", views.chokki, name="chokki"),
]
