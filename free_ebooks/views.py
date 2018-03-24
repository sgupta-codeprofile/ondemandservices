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
                start_save_data=add_ebook(title=request.POST['titles_name'],description=request.POST['ebook_description'])
                start_save_data.image = receive_data.cleaned_data['input_image']
                start_save_data.save()
                return HttpResponse('uploaded successfull')
            else:
                return HttpResponse("file uploading problem")
        else:
            form=input_ebook_detail()
            return render(request,'free_ebooks/add_ebooks.html',{'form':form})
    else:
        return HttpResponse('please login first')