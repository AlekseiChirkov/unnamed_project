# import datetime
# from datetime.relativedelta import relativedelta

from rest_framework import serializers

from .models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8,
        style={'input_type': 'password'},
        write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        exclude = ('last_login', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            home_address=validated_data['home_address'],
            city=validated_data['city'],
            region=validated_data['region'],
            country=validated_data['country'],
            phone=validated_data['phone'],
            age=validated_data['age'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'password': 'Passwords must match',
            })
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # age = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    # def get_age(self, instance):
    #     age = relativedelta(datetime.datetime.now(), instance.age).years
    #     return age


class ProfileSerializer(serializers.ModelSerializer):
    # age = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'
    #
    # def get_age(self, instance):
    #     age = relativedelta(datetime.datetime.now(), instance.age).years
    #     return age
