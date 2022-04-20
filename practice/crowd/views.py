from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework import viewsets, filters, generics, status

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    order_fields = ['created_at', 'total_cost']
    search_fields = ['title']
    filter_func = (filters.SearchFilter, filters.OrderingFilter)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer