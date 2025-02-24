from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("accounts/", include("allauth.urls")),
                path("_allauth/", include("allauth.headless.urls")),
                path("ninja/", include("backend.ninja_demo.urls")),
            ]
        ),
    ),
]
