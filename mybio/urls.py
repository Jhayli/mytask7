from django.urls import path
from .views import about, register


urlpatterns= [
    path("about-me/",about),
    path("register/", register)
]