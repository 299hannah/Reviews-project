from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user=models.OneToOneField(User, on_delete=models.CASCADE)
    # image = CloudinaryField('image')
    # description = models.TextField()
   
    user_name=models.CharField(max_length=300, null=True)
    bio= models.CharField(max_length=1000, null=True)

    # def __str__(self):
    #     return self.user

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.userprofile.save()
