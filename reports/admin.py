from django.contrib import admin

from reports.models import ExcelFileTemplate, ExcelFile, Report


class ExcelFileTemplatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExcelFileTemplate._meta.fields]

    class Meta:
        model = ExcelFileTemplate


class ExcelFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExcelFile._meta.fields]

    class Meta:
        model = ExcelFile


class ReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Report._meta.fields]
    
    class Meta:
        model = Report


admin.site.register(ExcelFileTemplate, ExcelFileTemplatesAdmin)
admin.site.register(ExcelFile, ExcelFileAdmin)
admin.site.register(Report, ReportAdmin)
