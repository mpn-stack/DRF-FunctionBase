from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer,ProductSerializerModelBase
from rest_framework.decorators import api_view

# Serializser
@api_view(['GET','POST', 'PUT', 'DELETE'])
def product_info(request, pk=None):
    if request.method=='GET':
        if pk is not None:
            queryset=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializer(queryset).data
            return Response(serializer, status=status.HTTP_200_OK)
        queryset=Product.objects.all()
        serializer=ProductSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method=='DELETE':
        if pk is not None:
            instance=get_object_or_404(Product, pk=pk)
            instance.delete()
            return Response ({'message':'the object has been deleted successfully.'}, status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        if pk is not None:
            queryset=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({'error':'bad request'}, status=status.HTTP_400_BAD_REQUEST)


## Model Based Serializer
@api_view(['GET','POST','PUT','DELETE'])
def product_info_model_base(request, pk=None):
    if request.method=='GET':
        if pk is not None:
            queryset=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializerModelBase(queryset).data
            return Response(serializer, status=status.HTTP_200_OK)
        queryset=Product.objects.all()
        serializer=ProductSerializerModelBase(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=ProductSerializerModelBase(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method=='DELETE':
        if pk is not None:
            instance=get_object_or_404(Product, pk=pk)
            instance.delete()
            return Response ({'message':'the object has been deleted successfully.'}, status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        if pk is not None:
            queryset = get_object_or_404(Product, pk=pk)
            serializer=ProductSerializerModelBase(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
    return Response({'error':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

