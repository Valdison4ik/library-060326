import os
import logging

from django.db.models import F
from django.utils import timezone

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

sql_logger = logging.getLogger('django.db.backends')
sql_logger.setLevel(logging.DEBUG)
sql_logger.addHandler(logging.StreamHandler())


from apps.library.models import BookModel, CategoryModel, AuthorModel, MemberRole, BookAuthorModel


# book = BookModel(title="Python Summary", published_date=timezone.now(), summary="Description", page_count=100)
# print(book.pk)
#
# category = CategoryModel(name='Python', slug='python')
# print(category.pk)
#
# print(book._state.adding)
#
# # Create, Update
# book.save()
#
# print(book._state.adding)


# book = BookModel.objects.create(
#     title="Pytest",
#     published_date=timezone.now(),
#     summary="Testing",
#     page_count=100
# )
#
# print(book)



# book = BookModel.objects.create(
#     title="Django",
#     published_date=timezone.now(),
#     summary="DRF",
#     page_count=100
# )
#
# book.page_count = 200
# book.save()


# category = CategoryModel.objects.get_or_create(
#     slug='trulala',
#     defaults={
#         'name': 'TRULALA'
#     },
# )
#
# print(category)


# book, created = BookModel.objects.update_or_create(
#     title = 'Django 6.1',
#     defaults={
#         'page_count': 300,
#     },
#     create_defaults={
#         'published_date': timezone.now(),
#         'summary': 'DRF',
#         'page_count': 300,
#     }
# )
#
# print(book, created)

# import random
#
# books = [
#     BookModel(
#         title=f'Book {i}{i}',
#         summary=f'Description of Book {i}',
#         published_date=timezone.now(),
#         page_count=random.randint(100, 1000),
#     )
#     for i in range(10)
# ]
#
#
# print(books)
#
# # for book in books:
# #     book.save()
#
#
# BookModel.objects.bulk_create(books)


# books = BookModel.objects.filter(page_count__gte=100)
# for book in books:
#     book.title = book.title.upper()
#     book.save()
#
# print(len(books))


# books = BookModel.objects.filter(page_count__gte=100).update(page_count=300)
# print(books)


# books = BookModel.objects.filter(page_count=300)
# for book in books:
#     book.title = f'A: {book.title.lower()}'
#     book.updated_at = timezone.now()
#
# BookModel.objects.bulk_update(books, ['title', 'updated_at'])

#
# books = BookModel.objects.filter(page_count__gte=300)
# for book in books:
#     book.page_count += 10
#     book.save(update_fields=['page_count', 'updated_at'])
#
# from django.db.models import F
#
# res = BookModel.objects.all().update(page_count=F('page_count') + 10)
#
# res = BookModel.objects.all().update(page_count=F('page_count') + 10)
# print(res)



# book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# book_2 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# print(book_1.page_count)
# book_1.page_count += 1
# book_1.save()
#
#
#
# book_2.page_count += 1
# book_2.save()
#
# book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# print(book_1.page_count)



# book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# book_2 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# print(book_1.page_count)
# book_1.page_count = F('page_count') + 1
# book_1.save()
#
#
#
# book_2.page_count = F('page_count') + 1
# book_2.save()
#
# book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
# print(book_1.page_count)
#
#



book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
book_1.refresh_from_db()
print(book_1.page_count)
book_1.page_count = F('page_count') + 1
book_1.save(update_fields=['page_count'])
book_1.save(update_fields=['page_count'])

book_1 = BookModel.objects.get(pk='8c497b57-737d-490e-b99b-04840d8b4f35')
print(book_1.page_count)










