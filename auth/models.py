from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    def upload_to(self, filename):
        return filename

    profile_pic = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                [
                    "jpg",
                    "png",
                    "jpeg",
                    "heic",
                ]
            )
        ],
    )
    phone_number = models.CharField(
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(regex=r"^\+?((2519)|(09)|(07)|(2517))\d{8}$"),
        ],
    )
    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = ["first_name"]
