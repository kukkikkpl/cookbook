from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import ImageField

from backend.authentication.utils import profile_directory_path


class CustomUserManager(UserManager):
    def get(self, *args, **kwargs):
        return super().select_related('profile').get(*args, **kwargs)


class User(AbstractUser):
    objects = CustomUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile',
    )
    public_name = models.CharField(max_length=150, null=True, unique=True)
    image = ImageField(upload_to=profile_directory_path, null=True, blank=True)
