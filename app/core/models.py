"""User Model"""

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                         PermissionsMixin,)

class UserManager(BaseUserManager):
    """User manager"""

    def create_user(self, email, password=None, **kwargs):
        """Create a new user and return the new user object"""

        if not email:
            raise ValueError('User email must provide a valid email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_superuser(self, email, password):
        "Create and return a new superuser"

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    """User model in the system"""
    email = models.CharField(max_length=255, unique=True, )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'