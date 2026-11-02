from django.db.models import Count

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.library.models import BookModel, CategoryModel, GenreModel
from apps.library.serializers import (BookListCreateSerializer,
                                      CategorySerializer,
                                      GenreSerializer,
                                      BookDetailSerializer
                                      )
from apps.library.pagination import BookPagination, CategoryLimitPagination, BookCursorPagination


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookListCreateSerializer
    pagination_class = BookCursorPagination
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer

    @action(detail=False, methods=['get'], url_path='books-count')
    def statistic(self, request):
        genres = GenreModel.objects.annotate(books_count=Count('books')).order_by('-books_count')
        data = [
            {'id': item.pk, 'name': item.name, 'count': item.books_count}
            for item in genres
        ]
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='books')
    def books_by_genre(self, request, pk=None):
        genre = self.get_object()
        books = BookModel.objects.filter(genres=genre).select_related().prefetch_related('genres__parent')
        serializer = BookDetailSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)