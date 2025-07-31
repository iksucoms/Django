

# Create your views here.
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request, "blog/index.html",
                  context={"posts":posts})
def detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,"blog/detail.html",context={"post":post})

