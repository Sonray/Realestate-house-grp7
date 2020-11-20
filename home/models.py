from django.db import models
from authentication.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class House(models.Model):
    image=CloudinaryField("photos", blank=True, null=True)
    name=models.CharField(max_length=400, null=True)
    description=models.TextField()
    bath=models.IntegerField(max_length=30, null=True, blank=True)
    bed=models.IntegerField(max_length=30, null=True, blank=True)
    price=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="houses")
    location=models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add = True, null =True)

    def save_house(self):
        self.save()

    def delete_house(self):
        self.delete()


class Review(models.Model):
    house = models.ForeignKey(House,on_delete = models.CASCADE,null=True, related_name="reviews")
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True, related_name="users")
    
    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()
    
    def __str__(self):
        return self.comment

