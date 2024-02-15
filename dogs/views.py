import django_filters
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

from dogs.models import Breed, Dog
from dogs.permissions import IsModer, IsOwner
from dogs.serializers import BreedSerializer, DogSerializer, BreedDetailSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def perform_create(self, serializer):
        new_dog = serializer.save(owner=self.request.user)
        new_dog.save()

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ('update', 'retrieve'):
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        elif self.action in ('destroy',):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


class BreedCreate(generics.CreateAPIView):
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        new_breed = serializer.save(owner=self.request.user)
        new_breed.save()


class BreedList(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['name', 'description']
    # ordering_fields = ['id', ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class BreedDetail(generics.RetrieveAPIView):
    serializer_class = BreedDetailSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]


class BreedUpdate(generics.UpdateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]


class BreedDelete(generics.DestroyAPIView):
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
