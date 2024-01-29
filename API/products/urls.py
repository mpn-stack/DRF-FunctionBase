from django.urls import path
from .views import product_info,product_info_model_base

urlpatterns=[
    path('',view=product_info, name='products'),
    path('model/<int:pk>/',view=product_info_model_base, name='productsmodel-single'),
    path('model/',view=product_info_model_base, name='productsmodel'),
]

