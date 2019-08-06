# normal forms and models forms
from django.forms import ModelForm
from main.models import User

class UserRegForm(ModelForm):
 	class Meta:
 		model=User
 		#fields="__all__"
 		fields=["username","password","email","phone","type"]