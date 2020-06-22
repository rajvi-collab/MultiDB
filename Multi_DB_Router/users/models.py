"""Model for the auth user creation."""
from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField


DATABASE = (
    ('data1_db', 'data1_db'),
    ('data2_db', 'data2_db'),
    ('data3_db', 'data3_db'),
    ('data4_db', 'data4_db'),
)

""" git clone https://github.com/vishalpolley/django-multidb.git"""


class CustomUserManager(BaseUserManager):
    """Cutomer Manager BaseUserManager."""

    def create_user(self, email, password):
        """Create user."""
        if not email:
            raise ValueError("Users must register an email")

        user = self.model(email=CustomUserManager.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create superuser."""
        user = self.create_user(email, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Using email instead of username."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_staff = models.BooleanField(default=False)
    database = MultiSelectField(choices=DATABASE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        """Meta Info."""

        app_label = 'users'
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUser'

    def __str__(self):
        """Str method to return ContactInfo name."""
        return self.email

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
