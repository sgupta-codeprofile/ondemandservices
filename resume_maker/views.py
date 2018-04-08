from django.shortcuts import render
from django.http import HttpResponse
from resume_maker.forms import Resume

def index(request):
    return render(request,'resume_maker/index.html',{'form':Resume()})
