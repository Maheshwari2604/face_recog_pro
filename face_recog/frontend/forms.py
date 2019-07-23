from django import forms 
from .models import Users
  
class UserForm(forms.ModelForm): 
  
    class Meta: 
        model = Users
        fields = ['name', 'user_img'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_img': forms.FileInput(attrs={'class': 'form-control'}),
        }