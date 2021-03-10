from django import forms
from django.contrib.auth.models import User
from blogger.models import Author, Category, Article


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="نام")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="نام خانوادگی")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="نام کاربری")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="رمز عبور")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class AuthorForm(forms.ModelForm):
    num_of_articles = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label="سن")

    class Meta:
        model = Author
        fields = ('age', 'picture')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
                               label="نام کاربری")
    password_error_messages = {'min_length': "رمزعبور حداقل باید ۶ کاراکتر باشد"}
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, min_length=6,
                               label="رمز عبور")
