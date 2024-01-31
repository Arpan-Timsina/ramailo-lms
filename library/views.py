from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import User, Book, BookDetail, BorrowedBook
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
        This viewset provides CRUD apis for books
    
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    """
    create,write,delete operations provided to AdminUser only for Books
    """
    
    action_permission_classes = {
        'destroy': [IsAuthenticated, IsAdminUser],
        'create': [IsAuthenticated, IsAdminUser],
        'update': [IsAuthenticated, IsAdminUser],
    }

    def get_permissions(self):
        """
        Override to dynamically determine the permission classes based on the action.
        """
        try:
            return [permission() for permission in self.action_permission_classes[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
        
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Delete associated BookDetail
        BookDetail.objects.filter(book=instance).delete()
        # Delete associated BorrowedBook
        BorrowedBook.objects.filter(book=instance).delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookDetailsViewSet(viewsets.ModelViewSet):
    """
        This viewset provides CRUD apis for BookDetails
    
    """
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailsSerializer
    
    permission_classes = [IsAuthenticated]


    """
    create,write,delete operations provided to AdminUser only for BooksDetails
    """
    
    action_permission_classes = {
        'destroy': [IsAuthenticated, IsAdminUser],
        'create': [IsAuthenticated, IsAdminUser],
        'update': [IsAuthenticated, IsAdminUser],
    }

    def get_permissions(self):
        """
        Override to dynamically determine the permission classes based on the action.
        """
        try:
            return [permission() for permission in self.action_permission_classes[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    
    """
        This viewset provides CRUD apis for Borowwing Books
        Update method is overriden  to free up the book if return_date is added
    
    """
    
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBooksSerializer
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)        
        if 'return_date' in request.data and instance.return_date is None:
            instance.book.available = True
            instance.book.save()
        return Response(serializer.data)

