from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Author
from django.shortcuts import render



def detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request,'blog/index.html',context={'one_article': blog})

def index(request):
    list_blog = Blog.objects.all()
    print(list_blog[0].picture.url)
    context = {'list_blog' : list_blog}
    
    return render(request,'blog/index.html',context)
