from django.forms import ModelForm
from django.forms import Textarea, EmailInput, TextInput
from django.utils.translation import gettext_lazy as _
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'fullname', 'email',
            'subject', 'description',
        ]
