import os
import logging

from django.db.models import F, Count, Avg, Min, Max, Sum, Subquery, OuterRef, ExpressionWrapper
from django.db.models.fields import FloatField, IntegerField, DurationField
from django.utils import timezone

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

sql_logger = logging.getLogger('django.db.backends')
sql_logger.setLevel(logging.DEBUG)
sql_logger.addHandler(logging.StreamHandler())


from apps.library.models import BookModel, CategoryModel, AuthorModel, MemberRole, BookAuthorModel, BorrowModel


# res = BookModel.objects.aggregate(total_books=Count('id'),
#                                   avg_pages=Avg('page_count'),
#                                   min_pages=Min('page_count'),
#                                   max_pages=Max('page_count')
#                                   )
# print(res)
#
#
# res = BookModel.objects.aggregate(
#     oldest=Min('published_date'),
#     newest=Max('published_date')
# )
#
# print(res)
#
#
# res = BookModel.objects.filter(category__slug='it').aggregate(
#     total_books=Count('id'),
#     avg_pages=Avg('page_count'),
# )
#
# print(res)
#
#
# res = BookModel.objects.filter(page_count__gte=10_000).aggregate(
#     total_books=Count('id'),
#     avg_pages=Avg('page_count'),
#     min_pages=Min('page_count', default=0),
#     max_pages=Max('page_count', default=0),
#     sum_pages=Sum('page_count')
# )

# print(res)


# authors = AuthorModel.objects.annotate(book_count=Count('books')).order_by('-book_count')
# for item in authors:
#     print(item, item.book_count)


# authors = AuthorModel.objects.annotate(book_count=Count('books')).filter(book_count__gt=3).order_by('-book_count')
# for item in authors:
#     print(item, item.book_count)


# books = BookModel.objects.values('category__name').annotate(books_count=Count('id')).order_by('-books_count')
# for book in books:
#     print(*book.values())

#
# book = BookModel.objects.annotate(
#     authors_n=Count('authors', distinct=True),
#     genres_n=Count('genres', distinct=True),
# ).get(pk='0132ea5b-4e7e-416f-9e55-87c678b93957')
#
# print(book.authors_n)
# print(book.genres_n)
# print(book)

# books = BookModel.objects.order_by(F('publisher__name').asc(nulls_last=True))
# print(*books, sep='\n')


# books = BookModel.objects.all()
# # print(books[:3])
# print(books[20:])
# # print(books[20:25])
# print(books[20:100:2])
#
# # print(books[10])
# # print(books[-1])
#
# print(books[::-1])


# avg_pages = BookModel.objects.aggregate(avg=Avg('page_count'))['avg']
# books = BookModel.objects.filter(page_count__gt=avg_pages)
#
# print(books)
#
#
# from django.db.models import Value
# sub_query = BookModel.objects.annotate(group=Value(1)).values('group').annotate(avg_pages=Avg('page_count')).values('avg_pages')
# res = BookModel.objects.filter(page_count__gt=Subquery(sub_query))
# print(res)


# sub_query = BookModel.objects.filter(
#     publisher=OuterRef('publisher'),
# ).values('publisher').annotate(avg_page=Avg('page_count')).values('avg_page')
#
#
#
# res = BookModel.objects.filter(page_count__lt=Subquery(sub_query))
# print(res)


# books = BookModel.objects.annotate(param=F('page_count') / 100)[:2]
# print(books[0].page_count, books[0].param)
# print(books[1].page_count, books[1].param)


# books = BookModel.objects.annotate(
#     param=ExpressionWrapper(
#         F('page_count') * 1.0 / 100,
#         output_field=FloatField())
# )[:2]
# print(books[0].page_count, books[0].param)
# print(books[1].page_count, books[1].param)

late = (
    BorrowModel.objects
    .filter(returned_date__gt=F('due_date'))
    .annotate(
        # delay=ExpressionWrapper(F('returned_date') - F('due_date'), output_field=DurationField())
        # delay=F('returned_date') - F('due_date')
    )
)

for borrow in late:
    print(
        borrow.book.title,
        borrow.delay
    )     # 3











