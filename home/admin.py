from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
from .models import Review
# Register your models here.
from .models import House,Review

# Register your models here.
admin.site.register(House)
admin.site.register(Review)
