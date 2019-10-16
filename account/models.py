from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #id,pw,email
    phoneNumber = models.TextField(max_length=13,blank=True)
    gender = models.CharField(max_length=2,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwars):
    instance.profile.save()
