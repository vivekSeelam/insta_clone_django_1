from django import forms
from .models import User


class UserSignUpForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={
                                   "placeholder": "Provide your full name",
                                   "class": "input-fields"
                               }
                           ), label="Full name")
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Provide your email",
                                    "class": "input-fields"
                                }
                            ), label="email")
    password = forms.CharField(required=True,
                               widget=forms.widgets.PasswordInput(
                                   attrs={
                                       "placeholder": "Provide your password",
                                       "class": "input-fields"
                                   }
                               ), label="Password")
    phone_num = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(
                                   attrs={
                                       "placeholder": "Provide your phone num",
                                       "class": "input-fields"
                                   }
                               ), label="phone_num")

    class Meta:
        model = User
        exclude = ('created_on', 'updated_on', 'is_active')
