from django.urls import path
from . import views



urlpatterns= [
    path("home", views.index, name="index"),
    path("view/<str:name>", views.view, name="view"),
    path("about/", views.details, name="detail_page"),
    path("add", views.add, name="add")
]
