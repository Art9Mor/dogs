from django.db import models

from users.models import NULLABLE, User


class Breed(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(**NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)


class Dog(models.Model):
    name = models.CharField(max_length=150)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dogs/', **NULLABLE)
    date_of_birth = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
