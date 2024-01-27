from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    count=serializers.IntegerField()
    company_name=serializers.CharField()
