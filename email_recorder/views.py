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
                try:
                    get_usr = email.objects.get(pk=request.user.email)
                    get_data = request.POST['cat_input']
                    if (get_data == 'Job_seekers'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Job_Seekers')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return HttpResponse('success added')
                    elif(get_data=='Earn_money'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Earn_Money')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return HttpResponse('success added')
                    else:
                        return HttpResponse('fail')
                except ObjectDoesNotExist:
                    start_load = email()
                    start_load.usr_email = request.user.email
                    start_load.save()
                    start_load_categories = email.objects.get(pk=request.user.email)
                    start_load_categories.cat_set.create(test='Job_Seekers')
                    start_load_categories.cat_set.create(test='Earn_Money')
                    start_load_categories.cat_set.create(test='Technology')
                    start_load_categories.cat_set.create(test='Political')
                    start_load_categories.cat_set.create(test='Crypto_currency')
                    return HttpResponse('You created your own directory now you can save the email')
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
