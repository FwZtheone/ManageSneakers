import email
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shoes, User
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators  import login_required
from django.shortcuts import redirect
from .forms.RegisterForm import RegisterForm

def home(request):
    return render(request,'blog/index.html')


@login_required
def list_shoes(request):
    
    return render(request,'blog/list_shoes.html')


@login_required
def profile(request):
    return render(request,'blog/profile.html')



def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # context = user authenticate
            form = RegisterForm(request.POST)
            storage = get_messages(request)
            if form.is_valid():
                user = User(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
                print(user)
                try:
                    user.save()
                    login(request,user)
                    messages.success(request,'account created succesful')
                    return redirect('/profile/')
                except ValueError:
                    messages.warning(request, ValueError )

        else:
            form  = RegisterForm()
        return render(request,'blog/register.html',{'form':form})
    else:
        return redirect('/')