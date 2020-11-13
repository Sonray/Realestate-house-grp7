from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    # House_id = models.ForeignKey(User,on_delete = models.CASCADE)
    Review_comment = models.TextField()
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()
    
    def __str__(self):
        return self.review

