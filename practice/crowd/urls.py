from django.urls import path, include
from .views import ProductViewSet, ProductDetailView, ProductFundingView

urlpatterns = [
    path('product/', ProductViewSet.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('product/<int:pk>/funding', ProductFundingView.as_view())
]

