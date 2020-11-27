from django.contrib.auth.models import User
from rest_framework import generics, permissions, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully created a new user.'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
