
from django.urls import include, path
from rest_framework import routers

from reports.views import (
<<<<<<< HEAD
    ReportViewSet, ArticleViewSet, ClothingSizeViewSet, ExcelFileViewSet
=======
    ReportViewSet, ArticleViewSet, ClothingSizeViewSet, ExcelFileViewSet, ReportListView
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
)

router = routers.DefaultRouter()
router.register('reports-list', ReportViewSet)
router.register('articles', ArticleViewSet)
router.register('clothing-sizes', ClothingSizeViewSet)
router.register('excel', ExcelFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
=======
    path('reports-list-filter/', ReportListView.as_view(), name='reports-list-filter')
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
]