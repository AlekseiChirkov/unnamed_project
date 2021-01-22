<<<<<<< HEAD
from rest_framework import status
=======
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

<<<<<<< HEAD
from reports.serializers import (
    ReportSerializer, ArticleSerializer, ClothingSizeSerializer, ExcelFileSerializer
)
from reports.models import (
    Report, Article, ClothingSize, ExcelFile
)
# from reports.utils import excel_data_in_model
=======
from .serializers import (
    ReportSerializer, ArticleSerializer, ClothingSizeSerializer, ExcelFileSerializer
)
from .models import (
    Report, Article, ClothingSize, ExcelFile
)
from .utils import excel_data_in_model
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13


class ExcelFileViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
<<<<<<< HEAD
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def create(self, request, *args, **kwargs):
        # excel_data_in_model(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save(user=self.request.user)
        return Response({
            'success': "File loaded successfully.",
        })
=======
    queryset = ExcelFile.objects.filter()
    serializer_class = ExcelFileSerializer

    def create(self, request, *args, **kwargs):
        excel_data_in_model(request)
        return Response({'success': "File loaded successfully."})
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13


class ClothingSizeViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
<<<<<<< HEAD
    queryset = ClothingSize.objects.all()
=======
    queryset = ClothingSize.objects.filter()
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
    serializer_class = ClothingSizeSerializer


class ArticleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
<<<<<<< HEAD
    queryset = Article.objects.all()
=======
    queryset = Article.objects.filter()
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
    serializer_class = ArticleSerializer


class ReportViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
<<<<<<< HEAD
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        report = self.queryset.all()
        serializer = self.serializer_class(report, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
=======
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
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
