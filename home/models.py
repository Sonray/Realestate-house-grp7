from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    Review_comment = models.TextField(max_length=255, blank=True)
    # House_id = models.ForeignKey(User,on_delete = models.CASCADE)
   
    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()
    
    def __str__(self):
        return self.review

