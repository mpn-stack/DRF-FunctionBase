from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def product_info(request):
    if request.method=='GET':
        #queryset = Product.objects.all()
        queryset= {'message':'it is just get method'}
        return Response(queryset)
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response (serializer.data)
    
    return Response({'message':'failed'})

