from django.contrib import admin

from reports.models import ExcelFileTemplates, ExcelFile, Report, Article, ClothingSize


class ExcelFileTemplatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExcelFileTemplates._meta.fields]

    class Meta:
        model = ExcelFileTemplates


class ExcelFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExcelFile._meta.fields]

    class Meta:
        model = ExcelFile


class ReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Report._meta.fields]
    
    class Meta:
        model = Report


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article


class ClothingSizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ClothingSize._meta.fields]

    class Meta:
        model = ClothingSize


admin.site.register(ExcelFileTemplates, ExcelFileTemplatesAdmin)
admin.site.register(ExcelFile, ExcelFileAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ClothingSize, ClothingSizeAdmin)
