from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    ReportSerializer, ArticleSerializer, ClothingSizeSerializer, ExcelFileSerializer, ExcelFileTemplatesSerializer
)
from .models import (
    Report, Article, ClothingSize, ExcelFile, ExcelFileTemplate
)


class ExcelFileTemplatesViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ExcelFileTemplate.objects.all()
    serializer_class = ExcelFileTemplatesSerializer


class ExcelFileViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
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


class ClothingSizeViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ClothingSize.objects.all()
    serializer_class = ClothingSizeSerializer


class ArticleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ReportViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        report = self.queryset.all()
        serializer = self.serializer_class(report, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'excel_file']
    search_fields = ['user', 'excel_file']
