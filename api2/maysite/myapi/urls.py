from rest_framework import routers
from .views import VloyatViewSet, MashenaViewSet, ZavodViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"vloyat", VloyatViewSet)
router.register(r"zavod", ZavodViewSet)
router.register(r"mashena", MashenaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
