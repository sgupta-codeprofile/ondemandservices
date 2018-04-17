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
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    elif(get_data=='Earn_money'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Earn_Money')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    elif(get_data=='Technology_lover'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Technology')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    elif(get_data=='Gadgets_lover'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Gadgets_lover')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    elif(get_data=='Political'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Political')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    elif(get_data=='Crypto_currency'):
                        s = email.objects.get(pk=request.user.email)
                        job_load = s.cat_set.get(test='Crypto_currency')
                        job_load.liststore_set.create(heavylist=request.POST['user_email'])
                        return render(request,'email_recorder/emailsendsuccessfully.html',{})
                    else:
                        return render(request,'bulk_email_sender/somethingwentwrong.html',{})
                except ObjectDoesNotExist:
                    start_load = email()
                    start_load.usr_email = request.user.email
                    start_load.save()
                    start_load_categories = email.objects.get(pk=request.user.email)
                    start_load_categories.cat_set.create(test='Job_Seekers')
                    start_load_categories.cat_set.create(test='Earn_Money')
                    start_load_categories.cat_set.create(test='Technology')
                    start_load_categories.cat_set.create(test='Gadgets_lover')
                    start_load_categories.cat_set.create(test='Political')
                    start_load_categories.cat_set.create(test='Crypto_currency')
                    return render(request,'email_recorder/startadd.html',{})
            else:

                return HttpResponse("error in database")

        else:
            return render(request, 'email_recorder/index.html', {'form': catagories()})
    else:
        return render(request,'free_ebooks/signinfirst.html',{})



def downloadlist(request):
    if request.user.is_authenticated:
        return render(request,'email_recorder/download_list.html',{'download_form':download_list()})
    else:
        return request(request,'free_ebooks/signinfirst.html',{})
