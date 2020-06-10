from rest_framework.routers import SimpleRouter
from .views import CardViewSet, UserViewSet
router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'users/<int:pk>/', UserViewSet)
router.register(r'cards', CardViewSet)
router.register(r'cards/<int:pk>/', CardViewSet)

urlpatterns = router.urls
