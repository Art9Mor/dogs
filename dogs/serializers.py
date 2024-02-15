from rest_framework import serializers
from dogs.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedDetailSerializer(serializers.ModelSerializer):
    dogs_of_breed = serializers.SerializerMethodField()

    def get_dogs_of_breed(self, breed):
        return [dog.name for dog in Dog.objects.filter(breed=breed)]

    class Meta:
        model = Breed
        fields = '__all__'


class BreedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('name',)


class DogSerializer(serializers.ModelSerializer):
    breed_detail = BreedNameSerializer(read_only=True, source='breed')
    dogs_with_same_breed = serializers.SerializerMethodField()

    def get_dogs_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    class Meta:
        model = Dog
        fields = '__all__'
