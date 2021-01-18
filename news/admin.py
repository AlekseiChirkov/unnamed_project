from django.contrib import admin

from news.models import News, NewsImage


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]

    class Meta:
        model = News


class NewsImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewsImage._meta.fields]

    class Meta:
        model = NewsImage


admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage, NewsImageAdmin)
