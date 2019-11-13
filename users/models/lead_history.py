from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from users.models.base import BaseModel
from users.models.leads import Lead

# Create your models here.

class LeadHistory(BaseModel):
    lead = models.ForeignKey(
        Lead,
        related_name='lead_history',
        db_index=True,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=10,
        unique=False,
        null=True
    )
    registered_phone_nos = models.CharField(
        max_length=100, 
        unique=False,
        null=True
    )
    more_details = models.CharField(
        max_length=1000, 
        unique=False,
        null=True,
    )
    reason = models.CharField(
        max_length=100, 
        unique=False,
        null=True
    )
    detailed_reason = models.CharField(
        max_length=1000, 
        unique=False,
        null=True
    )