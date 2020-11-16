from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from authentication.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.db.models import CharField


# Create your models here.


class House(models.Model):
    image=CloudinaryField("photos", blank=True, null=True)
    description=models.TextField()
    price=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
    user=models.ForeingKey(User, on_delete=models.CASCADE, related_name="houses")
    location=models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add = True, null =True)


#Profile

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    profile_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/', default="")
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    AUTH_PROFILE_MODULE = 'app.UserProfile'
    email=CharField(blank=True, max_length=200)

    def __str__(self):
            return f'{self.user.username} Profile'
    def save_profile(self):
        self.user
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


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
