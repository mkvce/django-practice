from django import forms
from django.contrib.auth.models import User
from blogger.models import Author, Category, Article

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class AuthorForm(forms.ModelForm):
    num_of_articles = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Author
        fields = ('age', 'picture')
