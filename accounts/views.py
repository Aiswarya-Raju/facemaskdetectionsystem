from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .forms import RegisterForm

def index(request):
    return render(request, 'accounts/index.html', {})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('social')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'accounts/login.html', {})

def home(request):
    return render(request, 'accounts/home.html', {})

    
def sanitizer(request):
    return render(request, 'accounts/sanitizer.html', {})

def social(request):
    return render(request, 'accounts/social.html', {})
    
def mask(request):
    return render(request, 'accounts/mask.html', {})

def payment(request):
    return render(request, 'accounts/payment.html', {})

def end(request):
    return render(request, 'accounts/end.html', {})

def logoutUser(request):
    logout(request)
    return redirect('index')