# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'bookdetails', views.BookDetailsViewSet)
router.register(r'borrowedbooks', views.BorrowedBooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
