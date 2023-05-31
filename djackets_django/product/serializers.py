from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'price',
            'image',
            'thumbnail',
            'date_added',
            'get_absolute_url',
            'get_image',
            'get_thumbnail'
            )