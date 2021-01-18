from django.contrib import admin
from .models import *

admin.site.register(DailySalesReport)
admin.site.register(WeeklySalesReport)
admin.site.register(MonthlySalesReport)
