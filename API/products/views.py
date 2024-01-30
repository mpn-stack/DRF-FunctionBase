from django.shortcuts import render,get_object_or_404
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer,ProductSerializerModelBase
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def product_info(request):
    if request.method=='GET':
        queryset=Product.objects.all()
        serializer=ProductSerializer(queryset, many=True).data
        return Response(serializer)
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
    return Response({'message':'failed'})


@api_view(['GET','POST'])
def product_info_model_base(request, pk=None):
    if request.method=='GET':
        if pk is not None:
            queryset=get_object_or_404(Product, pk=pk)
            serializer=ProductSerializerModelBase(queryset).data
            return Response(serializer)
        queryset=Product.objects.all()
        serializer=ProductSerializerModelBase(queryset, many=True).data
        return Response(serializer)
    
    if request.method=='POST':
        serializer=ProductSerializerModelBase(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
    return Response({'message':'failed'})

