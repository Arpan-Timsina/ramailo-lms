from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import User, Book, BookDetail, BorrowedBook
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailsSerializer

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBooksSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data.get('book')  # Retrieve book_id from request data
        user_id = request.data.get('user')  # Retrieve user_id from request data

        # Check if the book is already borrowed
        if BorrowedBook.objects.filter(book_id=book_id, return_date__isnull=True).exists():
            return Response({"error": "The book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user exists
        if not User.objects.filter(id=user_id).exists():
            return Response({"error": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the book exists
        if not Book.objects.filter(id=book_id).exists():
            return Response({"error": "Book does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Create borrowed book record
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)