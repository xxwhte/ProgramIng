from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # ('id', 'name', 'description', 'price', 'image', 'category')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
    fields = ('id', 'username', 'email')
