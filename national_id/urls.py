from django.urls import path, include
from rest_framework import routers

from national_id.views import NationalIdViewSet


router = routers.DefaultRouter()
router.register(r'NIDs', NationalIdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
