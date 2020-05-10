from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):

    '''Manager for User profiles'''
    def create_user(self,email,name,password=None):
        '''Create a New User profile'''
        if not email:
            raise ValueError('Users must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password) #this is hashed and then set it to database
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        '''Create and save new superuser with details'''
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database model for users in the system'''
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        '''Retreive full name of User'''
        return self.name

    def get_short_name(self):
        '''Retreive short name of User'''
        return self.name

    def __str__(self):
        '''return string representation of our User'''
        return self.email

class ProfileFeedItem(models.Model):
    '''profile status update'''
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Converts model into String'''
        return self.status_text
