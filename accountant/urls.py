from django.urls import path
from . import views


urlpatterns = [
    path('daily/', views.DailySalesReportView.as_view()),
    path('weekly/', views.WeeklySalesReportView.as_view()),
    path('monthly/', views.MonthlySalesReportView.as_view()),
]