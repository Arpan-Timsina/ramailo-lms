from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User, Book, BookDetail, BorrowedBook
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Delete associated BookDetail
        BookDetail.objects.filter(book=instance).delete()
        # Delete associated BorrowedBook
        BorrowedBook.objects.filter(book=instance).delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailsSerializer

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBooksSerializer
    # authentication_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # Custom logic to free up the book if return_date is added
        if 'return_date' in request.data and instance.return_date is None:
            instance.book.available = True
            instance.book.save()

        return Response(serializer.data)

