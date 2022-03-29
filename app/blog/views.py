from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Author
from django.shortcuts import render
from .forms.register.RegisterForm import RegisterForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate


def detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request,'blog/index.html',context={'one_article': blog})

def index(request):
    list_blog = Blog.objects.all()
    print(list_blog[0].picture.url)
    context = {'list_blog' : list_blog}
    
    return render(request,'blog/index.html',context)

def register(request):
    if request.method == 'POST':
        # context = user authenticate
        form = RegisterForm(request.POST)
        storage = get_messages(request)
        if form.is_valid():
            user = Author(name=form.cleaned_data['name'],lastname=form.cleaned_data['lastname'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            try:
                user.save()
                user_auth = authenticate(email=user.email,password=user.password)
                messages.success(request,'account created succesful')
                

            except:
                messages.warning(request, 'email already taken')

    else:
        form  = RegisterForm()
    return render(request,'blog/register.html',{'form':form})

