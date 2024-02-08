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
        """
        Create description using obj.name.
        """
        return f'the %s is grate!' % obj.name
    
    def create(self, validated_data):
        """
        Delete an existing `Product` instance.
        """
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.count = validated_data.get('count', instance.count)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.save()
        return instance
    

class ProductSerializerModelBase(serializers.ModelSerializer):
    #description = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
    
    def get_description(self, obj):
        """
        Create description using obj.name.
        """
        return f'the %s is grate!' % obj.name