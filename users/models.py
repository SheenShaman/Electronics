from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    name = models.CharField(max_length=50, verbose_name='Имя сотрудника', **NULLABLE)
    is_active = models.BooleanField(verbose_name='Активный пользователь', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
