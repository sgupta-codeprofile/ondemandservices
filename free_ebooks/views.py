from django.shortcuts import render
from django.http import HttpResponse
from .models import add_ebooks
from .forms import input_ebook_detail
# Create your views here.

def index(request):
    return render(request,'free_ebooks/index.html',{})


def add_ebooks(request):
    form=input_ebook_detail()
    return render(request,'free_ebooks/add_ebooks.html',{'form':form})