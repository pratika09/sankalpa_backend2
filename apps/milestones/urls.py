from rest_framework.routers import DefaultRouter
from .views import MilestoneViewSet

router = DefaultRouter()
router.register("milestone", MilestoneViewSet)

urlpatterns = router.urls
