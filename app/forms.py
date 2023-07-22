from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from .models import BlogPost

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels ={'first_name':'First Name','last_name':'Last Name','email':'Email',}
        # widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        #            'first_name':forms.TextInput(attrs={'class':'form-control'}),
        #            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        #            'email':forms.EmailInput(attrs={'class':'form-control'}),
        #            }

class LoginForm(AuthenticationForm):
    username = UsernameField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content']
        labeld = {'title':'Title','content':'Content'}
        widgets = {'content':forms.Textarea(attrs={'class':'form-control'}),
                   'title':forms.TextInput(attrs={'class':'form-control'}),
                   }
