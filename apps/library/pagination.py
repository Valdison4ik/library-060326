from rest_framework.pagination import (PageNumberPagination,
                                       LimitOffsetPagination,
                                       CursorPagination)
from rest_framework.response import Response


class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data,
            'page': self.page.number,
            'page_size': self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
        })


class CategoryLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_page_size = 10


class BookCursorPagination(CursorPagination):
    page_size = 10
    # ordering = '-created_at'
    ordering = ('-published_date', 'created_at')