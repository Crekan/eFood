from rest_framework import serializers

from .models import Restaurant


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['image', 'name', 'working_hours']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['image', 'name', 'working_hours']


class RestaurantDetailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Restaurant
        fields = ['image', 'name', 'working_hours', 'email']
