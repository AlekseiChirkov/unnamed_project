from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import *


class DailySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = DailySalesReportSerializers


class WeeklySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = WeeklySalesReportSerializers


class MonthlySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = MonthlySalesReportSerializers
