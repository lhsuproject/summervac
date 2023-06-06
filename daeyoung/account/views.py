from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthForm

# Create your views here.


#회원가입 html을 보여주는 함수
def regist(request):
    return render(request, 'regist.html')

# 회원가입을 위한 데이터를 저장하는 함수
def join(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("당신은 이미 회원입니다."+ str(user.email))
    
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email').lower()                        
            username = form.cleaned_data.get('username').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("/")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form']=form
        
    return render(request, 'regist.html', context)


#로그아웃
def logouts(request):
    logout(request)
    return redirect("/")

#로그인
def logins(request, *args, **kwargs):
    context={}
    
    user = request.user
    if user.is_authenticated:
        return redirect("/")
    
    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            # email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # user = authenticate(email=email, password=password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("/")
    else:
        form = AccountAuthForm()
        
    context['login_form'] = form
    
    return render(request, 'login.html',context)

def get_redirect_if_exists(request):
    redirect=None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

def myPage(request):
    user = request.user
    
    if user.is_authenticated is False:
        return redirect("login")
    
    return render(request, 'myPage.html', {'user': user})



        
                
