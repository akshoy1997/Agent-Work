from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from users.models.base import BaseModel
from users.models.agent import Agent

# Create your models here.

class Lead(BaseModel):
    agent = models.ForeignKey(
        Agent,
        related_name='leads',
        db_index=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30, 
        unique=False
    )
    phone_regex = RegexValidator( 
        regex=r'^\d{9,15}$', 
        message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
    )
    phone_number = models.CharField(
        _('Phone number'),
        max_length=10, 
        unique=False, 
        help_text=_('Only digits allowed'), 
        validators=[phone_regex]
    )
    address = models.CharField(
        max_length=250, 
        unique=False
    )
    status = models.CharField(
        max_length=10,
        unique=False
    )

    