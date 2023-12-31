from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form, 'error': form.errors})
  
def signin(request):
    if request.method == 'GET':
        return render(request, 'home.html', { 
            'form' : AuthenticationForm
        })
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home.html', { 
                'form' : AuthenticationForm,
                'error' : 'Username or password is incorrect',
            })
        else:
            login(request, user)
            return redirect('home')
            
def signout(request):
    logout(request)
    return redirect('home')