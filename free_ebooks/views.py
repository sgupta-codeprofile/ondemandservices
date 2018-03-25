from django.shortcuts import render
from django.http import HttpResponse
from free_ebooks.models import add_ebook
from .forms import input_ebook_detail


def index(request):
    send_data=add_ebook.objects.all()
    return render(request,'free_ebooks/index.html',{'go':send_data})


def add_ebooks(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            receive_data=input_ebook_detail(request.POST,request.FILES)
            if receive_data.is_valid():
                start_save_data=add_ebook(user_name=request.user.email,title=request.POST['title_name'],description=request.POST['ebook_description'])
                start_save_data.image = receive_data.cleaned_data['input_image']
                start_save_data.ebook_download=receive_data.cleaned_data['input_ebook']
                start_save_data.save()
                return render(request,'free_ebooks/file_upload_successfully.html',{})
            else:
                return HttpResponse("<h3 style='color:red;'>something went wrong please contact admin- shubhamguptaorg@gmail.com</h3>")
        else:
            form=input_ebook_detail()
            return render(request,'free_ebooks/add_ebooks.html',{'form':form})
    else:
        return render(request,'free_ebooks/signinfirst.html',{})


