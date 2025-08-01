from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Book


# Create your views here.
def index(request):
    books=Book.objects.all()

    return render(request, "library/index.html",context={"books":books})

def detail(request,pk):
    book=Book.objects.get(pk=pk)
    return render(request,"library/detail.html",context={"book":book})


def create(request):
    if request.method == "POST":
        postform=PostForm(request.POST)
        if postform.is_valid():
            post1=postform.save(commit=False)

            post1.save()
            return redirect('/library/')

    else:
        postform=PostForm()
    return render(request,template_name='library/postform.html',context={"postform":postform})