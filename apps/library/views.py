from django.shortcuts import render
from django.http import HttpResponse
from apps.library.models import BookModel


def index(request):
    books = BookModel.objects.earliest()
    return HttpResponse('Hello')


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})