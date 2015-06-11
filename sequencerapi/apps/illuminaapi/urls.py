from rest_framework.routers import DefaultRouter
from apps.illuminaapi.views import analyzeView,illuminaView,jobView

router = DefaultRouter()
router.register(r'illumina', illuminaView.IlluminaViewSet)
router.register(r'analyze', analyzeView.AnalyzeViewSet)
router.register(r'job', jobView.JobViewSet)

urlpatterns = router.urls

