from django.contrib import admin
from django.urls import include, path
from .api import api

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("admin/", admin.site.urls),
                path("accounts/", include("allauth.urls")),
                path("_allauth/", include("allauth.headless.urls")),
                path("", api.urls),
            ]
        ),
    ),
]