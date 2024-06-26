from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Shout Model
class Shout(models.Model):
    user = models.ForeignKey(
        User, related_name="shouts",
        on_delete=models.CASCADE
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="shout_like", blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )


# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
        upload_to="media/image", null=True, blank=True)
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100)
    linkedin_link = models.CharField(null=True, blank=True, max_length=100)
    youtube_link = models.CharField(null=True, blank=True, max_length=100)
    x_link = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_or_create_profile(cls, username):
        user, created = User.objects.get_or_create(username=username)
        profile, created = cls.objects.get_or_create(user=user)
        return profile, created

# Creat profile new user sign up


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

# Gallary for users images


class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/image')
    uploaded_at = models.DateTimeField(auto_now_add=True)
