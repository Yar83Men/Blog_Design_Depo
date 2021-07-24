from captcha.fields import CaptchaField
from django.forms import ModelForm
from django import forms

from .models import FeedBack


class FeedBackForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = FeedBack
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
