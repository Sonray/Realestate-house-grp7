from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
    pass

class House(models.Model):
    image=CloudinaryField("photos", blank=True, null=True)
    description=models.TextField()
    price=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
    user=models.ForeingKey(User, on_delete=models.CASCADE, related_name="houses")
    location=models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add = True, null =True)
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    House_id = models.ForeignKey(User,on_delete = models.CASCADE)
    Review_comment = models.TextField()
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()
    
    def __str__(self):
        return self.review

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Inquiry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inquire')
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    message = models.TextField(max_length=255, blank=True)
    def __str__(self):
        return f'{self.user.username} inquire'
    @receiver(post_save, sender=User)
    def create_user_inquiry(sender, instance, created, **kwargs):
        if created:
            Inquiry.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_inquiry(sender, instance, **kwargs):
        instance.Profile.save()
