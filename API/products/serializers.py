from rest_framework import serializers
from .models import Product
from django.utils import timezone
import uuid

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    description = serializers.SerializerMethodField()
    name=serializers.CharField()
    count=serializers.IntegerField()
    company_name=serializers.CharField()
    register_date=serializers.ReadOnlyField()

        
    def get_description(self, obj):
        return f'the %s is grate!' % obj.name
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    

class ProductSerializerModelBase(serializers.ModelSerializer):
    #description = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
    
    def get_description(self, obj):
        return f'the %s is grate!' % obj.name