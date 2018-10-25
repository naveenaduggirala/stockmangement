from django import forms
from .models import Categorie,Qunatite,Product

class ProductForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Product
		exclude = ()

class CategorieForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(CategorieForm, self).__init__(*args, **kwargs)
	class Meta:
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name'}),
            'label_name': forms.TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'label name'}), }

		model = Categorie
		exclude = ()



class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username',}))
	password = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password',}))

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
