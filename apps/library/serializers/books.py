from rest_framework import serializers
from apps.library.models import BookModel


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['title',]
