from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    ReportSerializer, ExcelFileSerializer, ExcelFileTemplatesSerializer,
    AddProductToExcelFileSerializer
)
from .models import (
    Report, ExcelFile, ExcelFileTemplate, AddProductToExcelFile
)


class ExcelFileTemplatesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ExcelFileTemplate.objects.all()
    serializer_class = ExcelFileTemplatesSerializer


class ExcelFileViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def list(self, request, *args, **kwargs):
        file = self.queryset.filter(user=self.request.user)
        serializer = self.serializer_class(file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        report = self.queryset.filter(user=self.request.user)
        serializer = self.serializer_class(report, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'excel_file']
    search_fields = ['user', 'excel_file']

    def list(self, request, *args, **kwargs):
        report = self.queryset.filter(user=self.request.user)
        serializer = self.serializer_class(report, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddProductToExcelFileViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = AddProductToExcelFile.objects.all()
    serializer_class = AddProductToExcelFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        for i, j in serializer.data.items():
            print(f"{str(i)}" + ": " + f"{str(j)}")
        return Response(serializer.data, status=status.HTTP_200_OK)
