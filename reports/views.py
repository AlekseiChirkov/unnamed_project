from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ReportSerializer, ArticleSerializer, ClothingSizeSerializer, ExcelFileSerializer
)
from .models import (
    Report, Article, ClothingSize, ExcelFile
)
from .utils import excel_data_in_model


class ExcelFileViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ExcelFile.objects.filter()
    serializer_class = ExcelFileSerializer

    def create(self, request, *args, **kwargs):
        excel_data_in_model(request)
        return Response({'success': "File loaded successfully."})


class ClothingSizeViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ClothingSize.objects.filter()
    serializer_class = ClothingSizeSerializer


class ArticleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Article.objects.filter()
    serializer_class = ArticleSerializer


class ReportViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Report.objects.filter()
    serializer_class = ReportSerializer


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['full_product_name', 'trademark',
                        'article', 'product_type', 'color', 'target_gender',
                        'clothing_size', 'composition', 'standard_no', 'status']
    search_fields = ['full_product_name', 'trademark',
                     'article', 'product_type', 'color', 'target_gender',
                     'clothing_size', 'composition', 'standard_no', 'status']
