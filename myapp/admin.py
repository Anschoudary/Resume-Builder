from django.contrib import admin
from .models import Resume, User

# Register your models here.

admin.site.register(User)
admin.site.register(Resume)