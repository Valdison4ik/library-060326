from rest_framework import serializers

from apps.library.models import PublisherModel


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel


