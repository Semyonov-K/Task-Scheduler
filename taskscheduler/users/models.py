from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Новая модель юзера с ролями."""
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_LIST = [
        (ADMIN, 'Admin role'),
        (USER, 'User role'),
        (MODERATOR, 'Moderator role')]

    first_name = models.CharField(
        'first name',
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=True
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(
        'О себе',
        blank=True
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_LIST,
        default='user'
    )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('pk',)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    def __str__(self):
        return self.username
