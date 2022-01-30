from dataclasses import field
from email.message import Message
from django import forms

from base.models import CustomerMessage


class MessageForm(forms.ModelForm):
    class Meta:
        model=CustomerMessage
        fields = '__all__'