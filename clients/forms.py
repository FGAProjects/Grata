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

    def clean_client(self):

        email = self.cleaned_data['email']

        if self.instance.id:

            if User.objects.filter(username=email).exclude(id=self.instance.id):

                raise forms.ValidationError('Usuário Já Cadastrado.')

class EditClientForm(UserChangeForm):

    sector = forms.CharField(max_length=70)

    class Meta:

        model = User
        fields = ('username', 'password','sector', 'first_name', 'last_name', )