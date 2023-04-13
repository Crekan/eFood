from rest_framework import generics

from .models import Books
from .serializers import BooksSerializer


class BooksView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
