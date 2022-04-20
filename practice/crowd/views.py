from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer, ProductFundingSerializer
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    ordering_fields = ['created_at', 'total_cost']
    search_fields = ['title']
    filter_backends = (SearchFilter, OrderingFilter)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductFundingView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFundingSerializer

    def put(self, request, *args, **kwargs):
        # 요청된 상품의 객체를 가져온다
        product = Product.objects.get(pk=kwargs['pk'])
        # 참여자 수를 증가시킨다.
        product.participants += 1
        # 총 펀딩 금액에 1회 펀딩 비용을 더한다.
        product.total_cost += product.funding_cost
        # 최종 수정된 상품 저장
        product.save()
        return Response(status=status.HTTP_200_OK)