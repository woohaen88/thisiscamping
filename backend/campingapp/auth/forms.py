from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-2",
                "type": "text",
                "placeholder": "ID를 입력하세요",
            }
        ),
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "type": "password",
                "placeholder": "비밀번호를 입력하세요",
            }
        ),
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-2",
                "type": "text",
                "placeholder": "ID를 입력하세요",
            }
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-2",
                "type": "email",
                "placeholder": "E-mail를 입력하세요",
            }
        ),
    )

    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "type": "password",
                "placeholder": "비밀번호를 입력하세요",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "type": "password",
                "placeholder": "비밀번호를 다시한번입력하세요",
            }
        ),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
