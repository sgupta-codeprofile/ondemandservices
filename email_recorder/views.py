from django.shortcuts import render
from django.http import HttpResponse
from email_recorder.forms import catagories,download_list
from email_recorder.models import cat,liststore,email


def index(request):
    return render(request,'email_recorder/index.html',{'form':catagories()})



def downloadlist(request):
    return render(request,'email_recorder/download_list.html',{'download_form':download_list()})
