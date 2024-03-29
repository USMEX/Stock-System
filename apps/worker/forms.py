from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import worker

# |-----| |-----| |-----| FORMULARIO DE REGISTRO|-----| |-----| |-----|
# |-----| Personalización del formulario registro de los        |-----| 
# |-----| trabajadores, esto con fines estéticos.               |-----|
# |-----| |-----| |-----| |----| |----| |----|  |-----| |-----| |-----|
class CreateUserForm(UserCreationForm):
	def __init__(self, *args,**kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({
				'class' : "form-control form-control-user", 
				'type' :"text", 
				'id' :"first_name", 
				'placeholder' :"First Name", 
				'name' :"first_name",
				'required' :True,
				})
		self.fields['last_name'].widget.attrs.update({
				'class' : "form-control form-control-user", 
				'type' :"text", 
				'id' :"last_name", 
				'placeholder' :"Last Name", 
				'name' :"last_name",
				'required' :True,
				})
		self.fields['username'].widget.attrs.update({
				'class' : "form-control form-control-user", 
				'type' :"email", 
				'id' :"exampleInputEmail", 
				'aria-describedby' :"emailHelp", 
				'placeholder' :"Email Address", 
				'name' :"email",
				})
		self.fields['password1'].widget.attrs.update({
				'class' : "form-control form-control-user", 
				'type' :"password", 
				'id' :"examplePasswordInput", 
				'placeholder' :"Password", 
				'name' :"password1",
				})
		self.fields['password2'].widget.attrs.update({
				'class' : "form-control form-control-user", 
				'type' :"password", 
				'id' :"exampleRepeatPasswordInput", 
				'placeholder' :"Repeat Password again", 
				'name' :"password2",
				})
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']