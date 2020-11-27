from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='registration'),
]
