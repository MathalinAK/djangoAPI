from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]

