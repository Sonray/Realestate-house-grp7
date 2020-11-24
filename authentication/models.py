from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):

    class User_Type(models.TextChoices):
        A_user = "USER", "User"
        Realtor = "REALTOR", "Realtor"

    username = models.CharField(max_length=280, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=280, blank=False)
    type = models.CharField('Type', max_length=30, choices=User_Type.choices, default=User_Type.A_user)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

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
=======
>>>>>>> main
