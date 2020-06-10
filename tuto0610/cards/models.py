from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Generate a token to each user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# card models
class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cardname = models.CharField(max_length=100)
    cardlimit = models.IntegerField(default=10000)

    def __str__(self):
        return self.cardname


