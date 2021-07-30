from django.shortcuts import redirect, render
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def registerUser(request):

    form = userRegisterForm()
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered, login to continue!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'authentication/register.html', context)

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome')
            return redirect('expenses:expenses')
        else:
            messages.info(request, 'Username OR Password was Incorrect')     

    context = {}
    return render(request, 'authentication/login.html', context)

def logoutUser(request):
    logout(request)
    messages.warning(request, f'You loged out')
    return redirect('login')
        

