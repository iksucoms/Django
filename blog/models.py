from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date=models.DateTimeField(auto_now_add=True,null=True)
    modified_date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return (f'게시글제목:{self.title} 게시글내용 - {self.content}')

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
