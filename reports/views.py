from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from reports.serializers import (
    ReportSerializer, ReportReadableSerializer, ArticleSerializer, ClothingSizeSerializer, ExcelFileSerializer
)
from reports.models import (
    Report, Article, ClothingSize, ExcelFile
)
from reports.utils import excel_data_in_model


class ExcelFileViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def create(self, request, *args, **kwargs):
        excel_data_in_model(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({
            'success': "File loaded successfully.",
        })


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

    def list(self, request, *args, **kwargs):
        news = self.queryset.all()
        serializer = ReportReadableSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
