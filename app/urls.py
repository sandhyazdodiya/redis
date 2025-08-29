from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CachedHelloWorld

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('cache/', CachedHelloWorld.as_view())
]