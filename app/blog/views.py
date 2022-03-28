from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Author
from django.shortcuts import render
from .forms.register.RegisterForm import RegisterForm


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
        if form.is_valid():
            print("ici")
            return HttpResponseRedirect('/blog/')
    else:
        form  = RegisterForm()
    return render(request,'blog/register.html',{'form':form})

