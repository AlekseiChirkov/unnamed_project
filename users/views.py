from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .serializers import *


# def activate(request, uid64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uid64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('https://www.vrmates.co/confirm')
#     else:
#         return HttpResponse('The link is inactive')


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            data['response'] = "Successfully created a new user. Please check your email and verify your account."
            data['email'] = user.email
            data['token'] = user.token
        else:
            data = serializer.errors
        return Response(data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        try:
            serializer = self.serializer_class(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'status': 0, 'message': 'Error on user update'})


class CurrentUserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ('email', )
