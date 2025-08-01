from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    uploaded_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'책제목:{self.title} - 책 내용 - {self.content}'

    def get_absolute_url(self):
        return f'/library/{self.pk}/'
