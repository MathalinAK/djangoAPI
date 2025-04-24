from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse
from rest_framework.reverse import reverse 
class BookListAPIView(APIView):
    """
    Handles GET and POST requests for listing all books and creating a new book.
    """
    def get(self, request, format=None):
        """
        List all books in the system.
        """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new book from the provided data.
        """
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a specific book.
    """
    def get(self, request, pk, format=None):
        """
        Retrieve a specific book by its ID.
        """
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a specific book by replacing its data.
        """
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        Partially update a specific book.
        """
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a specific book by its ID.
        """
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def api_root(request, format=None):
    """
    The root API endpoint, providing full URLs for navigation.
    """
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'book-detail': reverse('book-detail', kwargs={'pk': 1}, request=request, format=format),
    })
