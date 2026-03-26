from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer





class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        (1, 'SuperAdmin'),
        (2, 'Admin'),
        (3, 'User'),
    )

    user_type = models.PositiveSmallIntegerField(
    choices=USER_TYPES,
    default=3
     ) 
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)

    verification_token = models.CharField(max_length=100, null=True, blank=True)
    child_age = models.IntegerField(null=True, blank=True)
    
    child_name = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


    is_verified = models.BooleanField(default=False)


      
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
     

    objects = CustomUserManager()
    FAIRY_TYPES = (
        (1, 'Rainbow Fairy'),
        (2, 'Heart Fairy'),
        (3, 'Rainbow Unicorn '),
        (4, 'Star Fairy'),
        (5, 'Heart Unicorn'),
        (6, 'Fairy Wand'),
        
    )
    court_type = models.PositiveSmallIntegerField(
        choices=FAIRY_TYPES,
        default=1
    )
    MEMBERSHIP_TYPES = (
        (1, 'fairy time'),
        (2, 'fairy circle'),
        (3, 'fairy world'),
      
        
    )
    membership_type = models.PositiveSmallIntegerField(
        choices=MEMBERSHIP_TYPES,
        default=1
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


class globalmail(models.Model):
    mailtitel = models.CharField(max_length=100)
    mailbody = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_mail= models.EmailField(null=True, blank=True)


    def __str__(self):
        return self.mailtitel


@receiver(post_save, sender=globalmail)
def broadcast_new_mail(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "fairy_mail",
            {
                "type": "new_mail",
                "mail": {
                    "id": instance.id,
                    "mailtitel": instance.mailtitel,
                    "mailbody": instance.mailbody,
                    "created_at": str(instance.created_at),
                },
            },
        )


class MailReply(models.Model):
    mail = models.ForeignKey(globalmail, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reply_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.email} to {self.mail.mailtitel}"
    




class podcast(models.Model):
    podcasttitel = models.CharField(max_length=100)
    video = models.FileField(upload_to='podcast_videos/')
    thumbnail = models.ImageField(upload_to='podcast_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.podcasttitel
    
class uploadedpodcast(models.Model):
    podcast = models.ForeignKey(podcast, on_delete=models.CASCADE, related_name='uploaded_podcasts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.podcast.podcasttitel} uploaded by {self.user.email}"
