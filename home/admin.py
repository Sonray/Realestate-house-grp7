from django.contrib import admin
from .models import Inquiry,Review,House,UserProfile

admin.site.register(Inquiry)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(House)
