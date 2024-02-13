from django.shortcuts import render
from rest_framework import generics, viewsets

from dogs.models import Breed, Dog
from dogs.serializers import BreedSerializer, DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedCreate(generics.CreateAPIView):
    serializer_class = BreedSerializer


class BreedList(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedDetail(generics.RetrieveAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedUpdate(generics.UpdateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedDelete(generics.DestroyAPIView):
    queryset = Breed.objects.all()
