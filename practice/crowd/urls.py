from django.urls import path, include
from .views import ProductViewSet, ProductDetailView

urlpatterns = [
    path('product/', ProductViewSet.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view())
]

