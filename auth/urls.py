from django.urls import path
from channels.routing import URLRouter
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Register Viewsets here


urlpatterns = router.urls + []

auth_router = URLRouter([])
