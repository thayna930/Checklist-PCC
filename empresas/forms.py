from django import forms
from .models import Empresa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BootstrapStyleForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapStyleForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if isinstance(field.widget, (forms.TextInput, forms.DateInput, forms.EmailInput, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})

class UserProfile(BootstrapStyleForm):
    cidade = forms.CharField(label='Cidade', max_length=100)
    estado = forms.CharField(label='Estado', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20, required=False)
    cpf = forms.CharField(label='CPF', max_length=14, required=False, help_text='Digite apenas os números do CPF')
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False, help_text='Formato: AAAA-MM-DD')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'cidade', 'estado', 'telefone', 'cpf', 'data_nascimento', 'email', 'password1', 'password2']


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razao_social', 'email', 'cidade', 'estado', 'telefone', 'ramo_empresa']
