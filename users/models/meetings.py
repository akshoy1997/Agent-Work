from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from users.models.base import BaseModel
from users.models.leads import Lead

# Create your models here.

class Meeting(BaseModel):
    lead = models.ForeignKey(
        Lead,
        related_name='meetings',
        db_index=True,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=30, 
        unique=False
    )
    date = models.DateField(
        _(u"Conversation Date"), 
        blank=False
    )
    time = models.TimeField(
        _(u"Conversation Time"), 
        blank=False
    )
    venue = models.CharField(
        max_length=100, 
        unique=False
    )
    latitude = models.FloatField(
        unique=False,
        null=True
    )
    longitude = models.FloatField( 
        unique=False,
        null=True
    )