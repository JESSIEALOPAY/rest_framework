from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Reporter(models.Model):
    name= models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    biography= models.TextField(blank=True,null=True)

    def __str__(self) :
        return f"{self.name} {self.surname}"

class News(models.Model):
    author = models.ForeignKey(Reporter,on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=120)
    explanation = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=120)
    release_date = models.DateField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title