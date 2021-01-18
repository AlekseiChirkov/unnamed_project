from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class NewsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = News.objects.filter(published=True)
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        news = self.queryset.all()
        serializer = NewsReadableSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(requester=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('News id is required.')
        try:
            news = self.queryset.get(id=pk)
        except News.DoesNotExist:
            raise Http404
        else:
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class NewsImageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('News id is required.')

        try:
            image = self.queryset.get(id=pk)
        except NewsImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



