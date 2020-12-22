from django.urls import path

from .views import RegisterView, ProfileView, LoginAPIView


app_name = 'authentication'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('login/', LoginAPIView.as_view()),

]
