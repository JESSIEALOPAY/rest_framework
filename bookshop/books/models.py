from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    name= models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    explanation= models.TextField(blank=True,null=True) 

    created_date= models.DateField(auto_now_add=True)
    updated_date= models.DateField(auto_now=True)
    pub_date= models.DateTimeField()
    def __str__(self):
        return self.name


class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name="comments")
    
    commenter= models.ForeignKey(User , on_delete=models.CASCADE, related_name="user_comments")
    # commenter= models.CharField(max_length=50)
    comment= models.TextField(blank=True,null=True)

    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    reting= models.PositiveIntegerField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) :
        return self.comment
