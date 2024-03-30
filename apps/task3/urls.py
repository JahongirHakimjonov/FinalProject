from django.urls import path
from apps.task3.api_endpoints.Product.ProductListCreate.views import (
    ProductListCreateView,
)

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
]
