from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    class Meta():
        model=User
        fields=("username","first_name","last_name","age","email","password1","password2")

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['username'].widget.attrs['placeholder']="Username"
        
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['placeholder']="Password"
        
        self.fields['password2'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['placeholder']="Password"    


