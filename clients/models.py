from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ramal = models.CharField(max_length=4,null=True)
    sector = models.CharField(max_length=70,null=True)
    email = models.CharField(max_length=25,null=True,unique=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        client = Client(user=user)
        client.save()