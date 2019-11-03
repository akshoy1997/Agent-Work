from django import forms
from users.models.agent import Agent
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Agent
        fields = ['username', 'phone_number', 'email', 'password1', 'password2']