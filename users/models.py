from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

# Create your models here.
class UserSettings(models.Model):
    user = models.OneToOneField(User, related_name="settings")

    track_location = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserSettings.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserSettings.objects.get(user=instance)
            user_profile.delete()

class UserLocation(models.Model):
    user = models.OneToOneField(User)

    lat = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    lng = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    verbose_loc = models.CharField(max_length=300, default="")

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserLocation.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserLocation.objects.get(user=instance)
            user_profile.delete()