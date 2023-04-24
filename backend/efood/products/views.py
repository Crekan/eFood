from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ProductRetrivUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])
