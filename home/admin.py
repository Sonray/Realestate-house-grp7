from django.contrib import admin
<<<<<<< HEAD
from .models import *

admin.site.register(UserProfile)
from .models import Review
# Register your models here.
=======
from .models import House,Review

# Register your models here.
admin.site.register(House)
>>>>>>> 4c8ec86a9220764b7c20140ce80790886728b7e8
admin.site.register(Review)
