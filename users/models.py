from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35, **NULLABLE)
    telegram = models.CharField(max_length=150, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
