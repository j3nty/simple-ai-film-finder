from django.contrib import admin
from django.urls import path, include
from movies.views import home, generate_movie

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("generate_movie/", generate_movie, name="generate_movie"),
    path("accounts/", include("allauth.urls")),
]
