from django.contrib import admin

from .models import User


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'is_active']
    list_display_links = ['id', 'first_name', 'last_name', 'username']
    list_filter = ['is_active']
    search_fields = ['email', 'first_name', 'last_name']

    class Meta:
        model = User


admin.site.register(User, MyUserAdmin)
