from django.contrib import admin
from .models import Review,House,Inquiry

# Register your models here.

admin.site.register(Review)
admin.site.register(House)
admin.site.register(Inquiry)
from .models import *

admin.site.register(UserProfile)
