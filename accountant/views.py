from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import *


class DailySalesReportView(APIView):
    permission_classes = (AllowAny,)
    queryset = DailySalesReport.objects.all()
    serializer_class = DailySalesReportSerializers


class WeeklySalesReportView(APIView):
    permission_classes = (AllowAny,)
    queryset = DailySalesReport.objects.all()
    serializer_class = WeeklySalesReportSerializers


class MonthlySalesReportView(APIView):
    permission_classes = (AllowAny,)
    queryset = DailySalesReport.objects.all()
    serializer_class = MonthlySalesReportSerializers
