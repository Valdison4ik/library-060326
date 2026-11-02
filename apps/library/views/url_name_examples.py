from rest_framework import viewsets

from apps.library.models import BookModel, PublisherModel
from apps.library.serializers.publishers import PublisherSerializer
from apps.library.serializers.books import BookShortSerializer


class BookShortViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookShortSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer
