from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.conf import settings





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
