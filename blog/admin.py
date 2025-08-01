from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post , Category
# Register your models here.
# blog/admin.py
admin.site.register(Post)
admin.site.register(Category)