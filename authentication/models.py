from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
>>>>>>> 4c8ec86a9220764b7c20140ce80790886728b7e8
