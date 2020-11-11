from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    class User_Type(models.TextChoices):
        A_user = "USER", "User"
        Realtor = "REALTOR", "Realtor"

    type = models.CharField('Type', max_length=30, choices=User_Type.choices, default=User_Type.A_user)


class A_userManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.User_Type.A_user)


class RealtorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.User_Type.Realtor)


class A_user(User):
    objects = A_userManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.User_Type.A_user
        return super().save(*args, **kwargs)


class Realtor(User):
    objects = RealtorManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.User_Type.Realtor
        return super().save(*args, **kwargs)