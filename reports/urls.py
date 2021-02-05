from django.urls import include, path
from rest_framework import routers

from reports.views import (
    ReportViewSet, ExcelFileViewSet, ReportListView, ExcelFileTemplatesViewSet,
    AddProductToExcelFileViewSet
)

router = routers.DefaultRouter()
router.register('reports-list', ReportViewSet)
router.register('excel', ExcelFileViewSet)
router.register('excel-templates', ExcelFileTemplatesViewSet)
router.register('add-product', AddProductToExcelFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports-list-filter/', ReportListView.as_view(), name='reports-list-filter')
]