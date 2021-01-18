
from django.urls import include, path
from rest_framework import routers

from reports.views import (
    ReportViewSet, ArticleViewSet, ClothingSizeViewSet, ExcelFileViewSet
)

router = routers.DefaultRouter()
router.register('reports-list', ReportViewSet)
router.register('articles', ArticleViewSet)
router.register('clothing-sizes', ClothingSizeViewSet)
router.register('excel', ExcelFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]