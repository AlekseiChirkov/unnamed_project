from django.urls import path, include

from .views import *


app_name = 'users'


urlpatterns = [
    path('users/', UserRetrieveUpdateAPIView.as_view(), name='users'),
    path('users/me/', CurrentUserView.as_view(), name='me'),
    path('users/update/', UserUpdateAPIView.as_view(), name='update_user'),
    path('users/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('users/search/', UserListAPIView.as_view(), name='user-search'),

    # email verification
    # url(r'backend/activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
]