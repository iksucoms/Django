from django.shortcuts import render

from .models import Book


# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request, "library/index.html",context={"books":books})

def detail(request,pk):
    book=Book.objects.get(pk=pk)
    return render(request,"library/detail.html",context={"book":book})