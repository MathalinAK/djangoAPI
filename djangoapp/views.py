from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse
from rest_framework.reverse import reverse 
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    published_date = filters.DateFilter()
    published_date = filters.DateFilter()
    price = filters.NumberFilter()
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date','price']

class BookListAPIView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        filterset = BookFilter(request.GET, queryset=books)
        if filterset.is_valid():
            books = filterset.qs
        paginator = PageNumberPagination()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'book-detail': reverse('book-detail', kwargs={'pk': 1}, request=request, format=format),
    })
