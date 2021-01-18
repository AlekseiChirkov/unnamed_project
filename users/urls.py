from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('users/', UserRetrieveUpdateAPIView.as_view(), name='users'),
    path('users/me/', CurrentUserView.as_view(), name='me'),
    path('users/update/', UserUpdateAPIView.as_view(), name='update_user'),
    path('users/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/search/', UserListAPIView.as_view(), name='user-search'),
    path('users/request-password-reset-email/', RequestPasswordResetEmailAPIView.as_view(),
         name="request-password-reset"),
    path('users/password-reset-confirm/<uidb64>/<token>/',
         PasswordTokenCheckGenericAPIView.as_view(), name='password-reset-confirm'),
    path('users/password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),

    # email verification

    path('users/email-verify/', VerifyEmail.as_view(), name="email-verify"),

]
