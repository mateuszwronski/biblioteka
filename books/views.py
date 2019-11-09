from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from books.models import Book, Author
from books.permissions import ReadOnlyOrAdmin
from books.serializers import BookSerializers, AuthorSerializers


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [ReadOnlyOrAdmin]


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [IsAdminUser]


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [IsAdminUser]
