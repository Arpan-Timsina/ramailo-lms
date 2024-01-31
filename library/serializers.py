from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'membership_date']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published_date', 'genre']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'pages', 'publisher', 'language']

class BorrowedBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowedBook
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']


