from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
