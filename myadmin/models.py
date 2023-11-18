from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    profile_img = models.ImageField(upload_to=f"profile/", blank=True, null=True)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name()

    def name(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("myadmin:myadmin")


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_delete, sender=User)
def delete_set(sender, instance, **kwargs):
    user = User.objects.get(id=instance.id)
    for m in user.profile.all():
        m.delete()
