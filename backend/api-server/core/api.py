from ninja import NinjaAPI
from django.conf import settings
from django.http import HttpRequest

from abc import ABC, abstractmethod
from typing import Any, Optional


from ninja.errors import HttpError
from ninja.security.base import AuthBase
from ninja.utils import check_csrf
from ninja_demo.views import router as ninja_demo_router
from projects.views import project_router
from allauth.headless.contrib.ninja.security import x_session_token_auth



class APIKeyBase(AuthBase, ABC):
    openapi_type: str = "apiKey"
    param_name: str = "key"

    def __init__(self) -> None:
        self.openapi_name = self.param_name  # this sets the name of the security schema
        super().__init__()

    def __call__(self, request: HttpRequest) -> Optional[Any]:
        key = self._get_key(request)
        return self.authenticate(request, key)

    @abstractmethod
    def _get_key(self, request: HttpRequest) -> Optional[str]:
        pass  # pragma: no cover

    @abstractmethod
    def authenticate(self, request: HttpRequest, key: Optional[str]) -> Optional[Any]:
        pass  # pragma: no cover
class APIKeyCookie(APIKeyBase, ABC):
    openapi_in: str = "cookie"

    def __init__(self, csrf: bool = True) -> None:
        self.csrf = csrf
        super().__init__()

    def _get_key(self, request: HttpRequest) -> Optional[str]:
        if self.csrf:
            error_response = check_csrf(request)
            if error_response:
                raise HttpError(403, f"CSRF check Failed: {error_response}")
        return request.COOKIES.get(self.param_name)
class SessionAuth(APIKeyCookie):
    "Reusing Django session authentication"

    param_name: str = settings.SESSION_COOKIE_NAME

    def authenticate(self, request: HttpRequest, key: Optional[str]) -> Optional[Any]:
        if request.user.is_authenticated:
            return request.user

        return None

custom_auth = SessionAuth()


api = NinjaAPI(auth=[custom_auth, x_session_token_auth])

api.add_router("/ninja/", ninja_demo_router)
api.add_router("/projects/", project_router)