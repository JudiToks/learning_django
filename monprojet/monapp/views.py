from django.http import JsonResponse
from django.shortcuts import render
from .serializers import PersonnesSerializer, DogSerializer
from .models import Personnes, Dog
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

def bonjour(request) :
    return JsonResponse({'message':'Hello world!'})

@api_view(['GET'])
def getAllPersonnes(request) :
    personnes = Personnes.objects.all()
    serializer = PersonnesSerializer(personnes, many=True)
    return Response(serializer.data)

class DogListCreate(generics.ListCreateAPIView) :
    queryset = Dog.objects.all()
    serializer_class = DogSerializer