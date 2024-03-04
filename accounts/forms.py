from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password1']

        if commit:
            user = User.objects.create_user(email=user.email, password=user.password)
        return user

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
