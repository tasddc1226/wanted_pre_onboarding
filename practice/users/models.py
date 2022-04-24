from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    # create base user
    def create_user(self, email, nickname, name, password=None):
        if not email or not nickname:
            raise ValueError('Please provide email or nickname')
        if not name:
            raise ValueError('Please provide name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name
        )
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)

    # must have fields
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # use helper class
    objects = UserManager()

    USERNAME_FIELD = 'nickname'

    REQUEST_FIELD = ['email', 'name']

    def __str__(self):
        return self.nickname
