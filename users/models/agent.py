from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager

COMPANY_CHOICES = (
    ('ttu','TTU'),
)

class Agent(AbstractUser):
    username = models.CharField(
        max_length=30, 
        unique=False
    )
    email = models.EmailField(
        verbose_name="email", 
        max_length=60, 
        unique=True
    )
    phone_regex = RegexValidator( 
        regex=r'^\d{9,15}$', 
        message='Phone number must be entered in the format: "+999999999". Up to 10 digits allowed.'
    )
    phone_number = models.CharField(
        _('Phone number'),
        max_length=10, 
        unique=True, 
        help_text=_('Only digits allowed'), 
        validators=[phone_regex]
    )

    company = models.CharField(
        max_length=6, 
        choices=COMPANY_CHOICES, 
        default='TTU',
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email','company']

    objects = UserManager()

    def __str__(self):
        return self.username