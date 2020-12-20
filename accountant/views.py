from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import *


class DailySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = DailySalesReportSerializers
    permission_classes = (AllowAny,)


class WeeklySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = WeeklySalesReportSerializers
    permission_classes = (AllowAny,)


class MonthlySalesReportView(generics.ListCreateAPIView):
    queryset = DailySalesReport.objects.all()
    serializer_class = MonthlySalesReportSerializers
    permission_classes = (AllowAny,)
