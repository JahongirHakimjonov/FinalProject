from rest_framework.generics import ListCreateAPIView
from apps.task3.models import Product
from apps.task3.api_endpoints.Product.ProductListCreate.serializers import (
    ProductSerializer,
)


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


__all__ = ["ProductListCreateView"]
