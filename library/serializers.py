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
        fields = ['id', 'book', 'user', 'borrow_date', 'return_date']

    def validate(self, data):
        book= data.get('book')
        user = data.get('user')

        if BorrowedBook.objects.filter(book=book, return_date__isnull=True).exists():
            raise serializers.ValidationError({"Book":["The book is already borrowed."]})

        if not User.objects.filter(id=user.id).exists():
            raise serializers.ValidationError({"User":["User does not exist."]})

        if not Book.objects.filter(id=book.id).exists():
            raise serializers.ValidationError({"Book":["Book does not exist."]})

        return data 

    def update(self, instance, validated_data):
        return_date = validated_data.get('return_date')

        if return_date and instance.return_date is None:
            # If a return date is added and the book was borrowed (return_date was None)
            instance.return_date = return_date
            instance.save()

        return instance
