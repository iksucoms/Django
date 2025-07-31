from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date=models.DateTimeField()
    modified_date=models.DateTimeField()
    def __str__(self):
        return f'책제목:{self.title} - 책 내용 - {self.content}'
