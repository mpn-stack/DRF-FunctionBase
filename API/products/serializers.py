from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    description = serializers.SerializerMethodField()
    name=serializers.CharField()
    count=serializers.IntegerField()
    company_name=serializers.CharField()
    def get_description(self, obj):
        return f'the %s is grate!' % obj['name']

class ProductSerializerModelBase(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
    
    def get_description(self, obj):
        return f'the %s is grate!' % obj['name']