from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    ordering_fields = ['created_at', 'total_cost']
    search_fields = ['title']
    filter_backends = (SearchFilter, OrderingFilter)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer