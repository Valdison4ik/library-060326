from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.library.views.url_name_examples import BookShortViewSet, PublisherViewSet

app_name = 'example'

router = DefaultRouter()
router.register('books', BookShortViewSet, basename='books-example')
router.register('publishers', PublisherViewSet, basename='publishers')

urlpatterns = [
    path('', include(router.urls)),
]
