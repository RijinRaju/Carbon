from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError("user must have an email")

        user = self.model(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,username=None):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True,unique=True)
    password = models.CharField(max_length=150,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.username


class BaseUser(models.Model):
    username = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True,unique=True)
    password = models.CharField(max_length=150,null=True)