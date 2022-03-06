from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(
        max_length=100, help_text='Enter a title', db_column='News_Title')
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Blog'
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
