from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'writer',
            'description',
            'target_price',
            'expiry_date',
            'funding_cost',
            'total_cost',
        ]
        read_only_fields = ('participants', 'total_cost')

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'title',
            'writer',
            'total_cost',
            'getAchievement_rate',
            'getD_day',
            'description',
            'target_price',
            'getParticipants',
            'expiry_date',
            'funding_cost',
        ]

        read_only_fields = ('target_price', 'total_cost')

        extra_kwargs = {
            'expiry_date' : {'write_only': True},
            'funding_cost': {'write_only': True}
        }

class ProductFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = []