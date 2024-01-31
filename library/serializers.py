from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
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
        fields = "__all__"

    def validate(self, data):
        book= data.get('book')        
        borrowed_book = BorrowedBook.objects.filter(book=book).first()
        
        if borrowed_book and borrowed_book.is_book_freed:
            raise serializers.ValidationError({"Book":["The book is already borrowed."]})
        
        return data 
