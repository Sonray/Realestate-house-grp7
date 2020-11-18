from django.db import models
from authentication.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class House(models.Model):
    image=CloudinaryField("photos", blank=True, null=True)
    description=models.TextField()
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
    # House_id = models.ForeignKey(User,on_delete = models.CASCADE)
    review_comment = models.TextField()
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()
    
    def __str__(self):
        return self.review

