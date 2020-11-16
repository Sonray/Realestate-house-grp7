from django.db import models
<<<<<<< HEAD
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
=======
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

>>>>>>> 08c33c54434eab40017cda985d4cb93c8b0357b5
