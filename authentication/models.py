from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class User(AbstractUser):
     ACCOUNT_TYPE_CHOICES = (
        ('user', 'User'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'), 
     )
     account_type = models.CharField(max_length=20,choices=ACCOUNT_TYPE_CHOICES)
     username = models.CharField(max_length=100)
     email = models.EmailField(unique=True)
     is_blocked = models.BooleanField(default=False)
     
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ('username',)
     
     def __str__(self):
         return self.email
     
class Profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     full_name = models.CharField(max_length=300)
     bio = models.CharField(max_length=300)
     image = models.ImageField(default='default.jpg',upload_to='user_images')
     verified = models.BooleanField(default=False)
     
     def __str__(self):
         return self.user.email
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
          Profile.objects.create(user=instance)
          
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()
     