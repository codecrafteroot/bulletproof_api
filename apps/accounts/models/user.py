# thirdparty imports
from uuid import uuid4

# builtin imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# local imports
from ..managers import UserManager


class UserModel(AbstractUser):
    uuid = models.UUIDField(default=uuid4, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        ordering = ("pk",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        # Override the default __str__ of AbstractUser that returns username, which may
        # lead to leaking sensitive data in logs.
        return self.email