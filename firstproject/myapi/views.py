from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view()
def sayHello(request):
    return Response({"message": "Hello, world!"})

@api_view()
def drfRoute(request):
    return Response({'message': 'REST API designed by Django REST Framework'})

@api_view()
def api_root(request):
    return Response({
        'hello': reverse('hello', request=request),
        'drf': reverse('drf', request=request),
    })