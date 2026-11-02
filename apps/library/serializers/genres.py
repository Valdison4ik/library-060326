from rest_framework import serializers

from apps.library.models import GenreModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = '__all__'