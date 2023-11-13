import datetime
import re
from django import forms
from .services.EmpresaService import EmpresaService
from .services .ConexaoService import ConexaoService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services.MongoConnectionService import MongoConnectionService

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50, required= True)
    email = forms.CharField(max_length=20, required= True)
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    numero = forms.IntegerField(required= True)
    senha = forms.CharField(max_length=25, required= True, widget= forms.TextInput(attrs={'type' : 'password'}))
    ramo = forms.CharField(max_length=25, required= False)
    descricao = forms.CharField(max_length=50, required= False)
    telefone = forms.CharField(max_length = 15, required = True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
    site = forms.CharField(max_length=50, required= False)

    def valida_cnpj(self):
        connection = ConexaoService()
        bd = MongoConnectionService(connection, 'FoodShare')
        empresa = EmpresaService(FoodShareRepository(bd))
        cnpj = self.cleaned_data['cnpj']
        documento = empresa.findOne({'cnpj': cnpj})
        if documento:
            raise forms.ValidationError('CNPJ já cadastrado')

        return cnpj
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Email inválido')
    
        return email
            
        
    def clean_cnpj(self):
        
        cnpj = self.valida_cnpj()
        if len(cnpj) < 14  and ('-' not in cnpj and '/' not in cnpj):
            
            raise forms.ValidationError('CNPJ invalido')
            
        return cnpj
    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP invalido')
            
        return cep
    
    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Numero invalido')
            
        return numero
    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8 or not (any(char.isupper() for char in senha) and
                             any(char.islower() for char in senha) and
                             any(char.isdigit() for char in senha) and
                             any(char in "!@#$%^&*()_+{}\":;'<>.,\\-" for char in senha)):
            raise forms.ValidationError('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')

        return senha
            
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) < 11:
            raise forms.ValidationError('Telefone invalido')
            
        return telefone
   
    
class PessoaForm(forms.Form):
        nome = forms.CharField(max_length=25, required= True)
        cpf = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'placeholder':'999.999.999-99','id': 'cpf'}))
        email = forms.CharField(max_length=50, required= True)
        telefone = forms.CharField(max_length = 15, required = True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
        senha = forms.CharField(max_length=25, required= True, widget= forms.TextInput(attrs={'type' : 'password'}))
        cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
        data_nascimento  = forms.CharField(required= True,widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy', 'id': 'data_nascimento'}))
        numero = forms.IntegerField(required= True)
        social = forms.CharField(max_length=20, required= False)
        error_messages = {
        'nome_error' : 'Nome muito curto',
        'email_error' : 'Email invalido',
        'cnpj_error': 'CNPJ invalido',
        'cep_error': 'CEP invalido',
        'numero_error': 'Numero invalido',
        'senha_error': 'A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.',
        'telefone_error': 'Telefone Inválido'



        }
        def clean_senha(self):
            senha = self.cleaned_data['senha']
            if len(senha) < 8 or not (any(char.isupper() for char in senha) and
                             any(char.islower() for char in senha) and
                             any(char.isdigit() for char in senha) and
                             any(char in "!@#$%^&*()_+{}\":;'<>.,\\-" for char in senha)):
                raise forms.ValidationError('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')

        
            return senha
        def clean_nome(self):
            nome = self.cleaned_data['nome']
            if len(nome) < 5:
                raise forms.ValidationError('Nome muito curto')
            return nome
        def clean_telefone(self):
            telefone = self.cleaned_data['telefone']
            if len(telefone) < 11:
                raise forms.ValidationError('Telefone invalido')
            
            return telefone
        def clean_cpf(self):
            cpf = self.cleaned_data['cpf']
            if len(cpf) < 14:
                raise forms.ValidationError('CPF invalido')
            return cpf
        def clean_email(self):
            email = self.cleaned_data['email']
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                raise forms.ValidationError('Email inválido')
    
            return email
        def clean_cep(self):
            cep = self.cleaned_data['cep']
            if len(cep) < 8:
                raise forms.ValidationError('CEP invalido')
                
            
            return cep
        def clean_numero(self):
            numero = self.cleaned_data['numero']
            if numero < 1:
                raise forms.ValidationError('Numero invalido')
            return numero
        def validar_data(data):
            pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
            if not re.match(pattern, data):
                raise forms.ValidationError('Data invalida')

            dia, mes, ano = map(int, data.split('/'))

            if (mes in [4, 6, 9, 11] and dia > 30) or (mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) and dia > 29) or (mes == 2 and dia > 28):
                raise forms.ValidationError('Data invalida')

            return data
        
class DoacaoForm(forms.Form):
    nome = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'nome'}))
    telefone = forms.CharField(max_length = 14, required = True, widget=forms.TextInput(attrs={'name': 'telefone','placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
    email = forms.CharField(max_length=50, required= True) 
    endereco = forms.CharField(max_length=100)
    numero = forms.IntegerField(required=True)
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    estado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Estado'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    valor = forms.IntegerField(required=True)

    def clean_cep(self):
            cep = self.cleaned_data['cep']
            if len(cep) < 8:
                raise forms.ValidationError('CEP invalido')
                
            
            return cep
    def clean_nome(self):
            nome = self.cleaned_data['nome']
            if len(nome) < 5:
                raise forms.ValidationError('Nome muito curto')
            return nome
    def clean_telefone(self):
            telefone = self.cleaned_data['telefone']
            if len(telefone) < 11:
                raise forms.ValidationError('Telefone invalido')
    def clean_email(self):
            email = self.cleaned_data['email']
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                raise forms.ValidationError('Email inválido')
    def clean_numero(self):
            numero = self.cleaned_data['numero']
            if numero < 1:
                raise forms.ValidationError('Numero invalido')
            return numero
    def clean_valor(self):
            valor = self.cleaned_data['valor']
            if valor < 1:
                raise forms.ValidationError('Valor invalido')
            return valor