from ninja import NinjaAPI
from ninja.security import django_auth

from ninja_demo.views import router as ninja_demo_router
from projects.views import project_router
from allauth.headless.contrib.ninja.security import x_session_token_auth


api = NinjaAPI(auth=[django_auth, x_session_token_auth])

api.add_router("/ninja/", ninja_demo_router)
api.add_router("/projects/", project_router)