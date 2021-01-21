
from django.urls import include, path
from rest_framework import routers

from reports.views import (
    ReportViewSet, ArticleViewSet, ClothingSizeViewSet, ExcelFileViewSet, ReportListView
)

router = routers.DefaultRouter()
router.register('reports-list', ReportViewSet)
router.register('articles', ArticleViewSet)
router.register('clothing-sizes', ClothingSizeViewSet)
router.register('excel', ExcelFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports-list-filter/', ReportListView.as_view(), name='reports-list-filter')
]