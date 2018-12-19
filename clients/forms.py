from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class ClientSignUp(UserCreationForm):

    ramal = forms.CharField(max_length=4)
    sector = forms.CharField(max_length=70)
    email = forms.CharField(max_length=70)

    class Meta:
        model = User
        fields = ('username', 'ramal', 'sector','email', 'password1', 'password2', )

class EditClientForm(UserChangeForm):

    sector = forms.CharField(max_length=70)

    class Meta:

        model = User
        fields = ('username', 'password','sector', 'first_name', 'last_name', )