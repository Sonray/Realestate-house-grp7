from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
from .models import Review
# Register your models here.
admin.site.register(Review)
