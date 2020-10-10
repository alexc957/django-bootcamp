# check for unique email and username 
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
          
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    password2 = forms.CharField(
        label="Confirm password Password",
        widget=forms.PasswordInput(
           
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("this is an invalid user, please pick other ")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("this email is already in use")
        return email 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    #def clean(self): #
    #    username = self.cleaned_data.get("username")
    #    password = self.cleaned_data.get("password")


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("this is an invalid user")

        return username


