from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserManager
from .utils import upload_avatar_to, NOTIFICATION_TYPES, NOTIFICATION_STATUS


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email


class EmailAddress(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='email_addresses')
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)
    primary = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class EmailConfirmation(models.Model):
    email = models.ForeignKey('EmailAddress', on_delete=models.CASCADE)
    key = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email.email


class PasswordReset(models.Model):
    email = models.EmailField(unique=True)
    enc_email = models.CharField(verbose_name='Encrypted Email', max_length=500, unique=True)
    token = models.CharField(max_length=500)


    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to=upload_avatar_to, default='avatars/default.jpg')
    title = models.CharField(max_length=60, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=60, blank=True)
    followers = models.ManyToManyField('User', related_name='followers', blank=True)
    following = models.ManyToManyField('User', related_name='following', blank=True)

    def __str__(self):
        return f"<Profile <User {self.user.username}>>"


class FollowNotification(models.Model):
    fromuser = models.ForeignKey('User', on_delete=models.CASCADE, related_name="from user+")
    touser = models.ForeignKey('User', on_delete=models.CASCADE, related_name="to user+")
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=10, choices=NOTIFICATION_STATUS, default='unread')

    def __str__(self):
        return f"<Follow Notification: {self.fromuser.username}-{self.touser.username}>"


class VoteNotification(models.Model):
    fromuser = models.ForeignKey('User', on_delete=models.CASCADE, related_name="from user+")
    touser = models.ForeignKey('User', on_delete=models.CASCADE, related_name="to user+")
    voted_post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=10, choices=NOTIFICATION_STATUS, default='unread')

    def __str__(self):
        return f"<Post Notification: {self.fromuser.username}-{self.touser.username}({self.post})>"
