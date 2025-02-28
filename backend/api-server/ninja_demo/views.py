from ninja import Router
from ninja.security import django_auth

from allauth.headless.contrib.ninja.security import x_session_token_auth

router = Router(tags=["API1"])

@router.get("/api/add", auth=[django_auth, x_session_token_auth])
def add(request, x: float, y: float):
    return {"result": x + y +3}
