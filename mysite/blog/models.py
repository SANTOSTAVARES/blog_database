from turtle import title, update
from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250) #Post title field.
    slug = models.SlugField(max_length=250, #This is used to make URL.
        unique_for_date='publish') #Add date to URL publish.
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='blog_posts') #If delete user from database, the SQL delete all its posts.
    body = models.TextField() #post content.
    publish = models.DateTimeField(default=timezone.now) #Advise when the post was published.
    created = models.DateField(auto_now_add=True) #Advise when the post was created.
    update = models.DateTimeField(auto_now=True) #Advise when the post was updated.
    status = models.CharField(max_length=10, #Show the status post.
        choices=STATUS_CHOICES, #The post status has to be specified.
        default='draft')

class Meta:
    ordering = ('-publish',) #Sort results following the 'publish' field (old first).

def __str__(self):
    return self.title