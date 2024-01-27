from django.urls import path
from .views import product_info

urlpatterns=[
    path('',view=product_info, name='products'),
]

