from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio= models.CharField(max_length=300 , blank=True )
    city= models.CharField(max_length=200,blank=True )
    foto= models.ImageField(blank=True, null=True)

    def __str__(self) :
        return self.user.username
    
    class Meta:
        verbose_name_plural="Profiller" #admin pageteki adı nbu yaptık
    
    def save(self, *args, **kwargs):
        ### Image Resize
        super().save(*args, **kwargs)
        if self.foto:
            img= Image.open(self.foto.path)
            if img.height>600 or img.width>600:
                output_size=(600,600)
                img.thumbnail(output_size)
                img.save(self.foto.path)

class ProfileStatus(models.Model):
    user_profile= models.ForeignKey(Profile,on_delete=models.CASCADE)
    status_message= models.CharField(max_length=250)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_message
        

