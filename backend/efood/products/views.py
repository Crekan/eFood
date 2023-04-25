from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer, ProductCreateSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])
