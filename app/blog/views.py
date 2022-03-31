from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Author
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

def detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request,'blog/index.html',context={'one_article': blog})

def index(request):
    list_blog = Blog.objects.all()
    print(list_blog[0].picture.url)
    context = {'list_blog' : list_blog}
    
    return render(request,'blog/index.html',context)


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
                user = Author(name=form.cleaned_data['name'],lastname=form.cleaned_data['lastname'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
                try:
                    # user.save()
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