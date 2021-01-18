from rest_framework import serializers
from .models import News, NewsImage
from users.serializers import UserSerializer


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = ['title', 'text', 'created_date', 'published', 'images']

    def create(self, validated_data):
        images_data = self.context.get('request').FILES
        news_post = News.objects.create(
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            created_date=validated_data.get('created_date')
        )
        for image_data in images_data.values():
            NewsImage.objects.create(news_post=news_post, image=image_data)
        return news_post


class NewsReadableSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    images = NewsImageSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = '__all__'
