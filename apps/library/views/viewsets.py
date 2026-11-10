from django.db.models import Count

from rest_framework import viewsets, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions,)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.library.models import BookModel, CategoryModel, GenreModel
from apps.library.serializers import (BookListCreateSerializer,
                                      CategorySerializer,
                                      GenreSerializer,
                                      BookDetailSerializer
                                      )
from apps.library.pagination import BookPagination, CategoryLimitPagination, BookCursorPagination

from apps.library.permissions import IsLibrarian, StrictDjangoModelPermissions, CanGetStatistics


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsLibrarian]
    queryset = BookModel.objects.all()
    serializer_class = BookListCreateSerializer
    pagination_class = BookCursorPagination
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'



class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [~IsAdminUser] # ~, |, &
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitPagination

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]



class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer

    @action(detail=False, methods=['get'], url_path='books-count', permission_classes=[CanGetStatistics])
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