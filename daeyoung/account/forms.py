from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account

#회원가입 폼
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='이메일 주소를 추가하세요.')
    
    class Meta:
        model=Account
        fields = ('email','username','phone','name','password1','password2','school', 'grade', 'major')
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} 은 이미 사용중 ")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"usenrID {username} 은 이미 사용중 ")
    
#로그인 인증 폼

class AccountAuthForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('username','password')
        
    def clean(self):
        if self.is_valid():
            # email = self.cleaned_data['email']
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("로그인 실패")
