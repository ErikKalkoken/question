from math import fabs
from pickle import FALSE
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    body = RichTextField(blank=False, null=False) 
    category = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.title)

class Answer(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    answer = RichTextField(blank=False, null=False)
    post = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)  

class FeedBack(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
       return str(self.name)


class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
       return str(self.user)