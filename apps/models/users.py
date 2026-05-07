from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    phone = CharField(max_length=13, unique=True)
    class Role(TextChoices):
        ADMIN = 'admin', 'ADMIN'
        AUTHOR = 'author', 'AUTHOR'
        READER = 'reader', 'READER'

    role = CharField(max_length=15, choices=Role.choices, default=Role.READER)

    objects = CustomUserManager()
