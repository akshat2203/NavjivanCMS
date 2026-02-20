from rest_framework.routers import DefaultRouter
from .views import AadhaarViewSet, PANViewSet

router = DefaultRouter()
router.register(r'aadhaar', AadhaarViewSet, basename='aadhaar')
router.register(r'pan', PANViewSet, basename='pan')

urlpatterns = router.urls
