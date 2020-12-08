from rest_framework import serializers
from .models import *


class DailySalesReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailySalesReport
        fields = '__all__'


class WeeklySalesReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeeklySalesReport
        fields = '__all__'


class MonthlySalesReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = MonthlySalesReport
        fields = '__all__'
