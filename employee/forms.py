from django import forms
from .models import employee
from django.forms import ModelForm
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwrgs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('this user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('the entered pass word is incorrect')
            if not user.is_active:
                raise forms.ValidationError('this user is not active')
        return super(UserLoginForm,self).clean(*args,**kwrgs)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model= employee
        fields= '__all__'
    

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label ="select"  
        
