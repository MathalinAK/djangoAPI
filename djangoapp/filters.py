import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    published_date = django_filters.DateFilter()
    price = django_filters.NumberFilter()
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price']
