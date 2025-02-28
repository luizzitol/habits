from ninja import NinjaAPI
from ninja_demo.views import router as ninja_demo_router

api = NinjaAPI()

api.add_router("/ninja/", ninja_demo_router)