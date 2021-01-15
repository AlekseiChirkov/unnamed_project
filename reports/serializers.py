from rest_framework import serializers

from reports.models import (
    Report, Article, ClothingSize, ExcelFile
)


class ExcelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = '__all__'
        # fields = ['excel_file']


class ClothingSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingSize
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportReadableSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    clothing_size = ClothingSizeSerializer()
    excel_file = ExcelFileSerializer()

    class Meta:
        model = Report
        fields = '__all__'

