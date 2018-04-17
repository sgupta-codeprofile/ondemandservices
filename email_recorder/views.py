from django.shortcuts import render
from django.http import HttpResponse
from email_recorder.forms import catagories,download_list
from email_recorder.models import cat,liststore,email
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            received_data=catagories(request.POST)
            if received_data.is_valid():
                start_load=email()
                start_load.usr_email=request.user.email
                start_load.save()
                try:
                    get_usr=email.objects.get(pk=request.user.email)
                    get_usr.cat_set.create(test=request.POST['cat_input'])
                    get_usr.save()
                    get_cat=cat.objects.get(test=request.POST['cat_input'])
                    get_cat.liststore_set.create(heavylist=request.POST['user_email'])
                    get_cat.save()
                except:
                    return HttpResponse("exception run report is sumbitted to admin")
                return HttpResponse('success')
            else:
                return HttpResponse("eroor in database")

        else:
            return render(request, 'email_recorder/index.html', {'form': catagories(), 'success_urna': 1})
    else:
        return render(request,'free_ebooks/signinfirst.html',{})



def downloadlist(request):
    if request.user.is_authenticated:
        return render(request,'email_recorder/download_list.html',{'download_form':download_list()})
    else:
        return request(request,'free_ebooks/signinfirst.html',{})
