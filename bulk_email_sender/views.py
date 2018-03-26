from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from .forms import Sendmail,user_email_list,send_in_bulk_email
from bulk_email_sender.models import Maildata,email_list,Maildata_send_in_bulk


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.email == 'geekydirect@gmail.com' and request.user.username == 'geekydirect':
                check_detail=Sendmail(request.POST)
                if check_detail.is_valid():
                    data_save_start=Maildata(sender_data=request.user.email,reciver_data=request.POST['reciver'],subject_data=request.POST['subject'],message_data=request.POST['message'])
                    data_save_start.save()
                    try:
                        port=587
                        server=smtplib.SMTP('smtp.gmail.com',port)
                        server.starttls()
                        server.login('geekydirect@gmail.com','Password')  #Enter password of your gmail account
                        ready_msg = MIMEText(request.POST['message'])
                        ready_msg['subject']=request.POST['subject']
                        server.sendmail('geekydirect@gmail.com',request.POST['reciver'],ready_msg.as_string())
                        server.quit()
                        return HttpResponse('email send successfully ')
                    except:
                        return HttpResponse('Something went wrong pls contact admin:shubhamguptaorg@gmail.com')
                else:
                    return HttpResponse('we catch something went wrong in form validation pls contact admin')

            else:
                return HttpResponse("<h4 style='color:red;'>This application is for only admin</h4><p style='color:green;'>WE are currently working on this application to make generic</p>")
        else:
            return render(request,'bulk_email_sender/index.html',{'form':Sendmail()})

    else:
        return render(request,'bulk_email_sender/signinfirst.html',{})


def add_email(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            get_email=user_email_list(request.POST)
            if request.user.email == 'geekydirect@gmail.com' and request.user.username == 'geekydirect':
                if get_email.is_valid():
                    start_save_email=email_list(userlist=request.POST['add_email'])
                    start_save_email.save()
                    return HttpResponse('email sucessfully added')
                else:
                    return HttpResponse('something went wrong in form validation pls contact admin: shubhamguptaorg@gmail.com')
            else:
                return HttpResponse("<h4 style='color:red;'>This application is for only admin</h4><p style='color:green;'>WE are currently working on this application to make generic</p>")
        else:
            return render(request,'bulk_email_sender/add_emails.html',{'addemail':user_email_list()})
    else:
        return render(request,'bulk_email_sender/signinfirst.html',{})


def send_in_bulk(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.email == 'geekydirect@gmail.com' and request.user.username == 'geekydirect':
                check_detail=send_in_bulk_email(request.POST)
                if check_detail.is_valid():
                    data_save_start=Maildata_send_in_bulk(sender_data_send_in_bulk=request.user.email,
                                                          reciver_data_send_in_bulk='bulk_standard',
                                                          subject_data_send_in_bulk=request.POST['subject_send_in_bulk'],
                                                          message_data_send_in_bulk=request.POST['message_send_in_bulk'])
                    data_save_start.save()
                    temp=email_list.objects.all()
                    try:
                        port=587
                        count=0
                        server=smtplib.SMTP('smtp.gmail.com',port)
                        server.starttls()
                        server.login('geekydirect@gmail.com','Password') #enter you gamil password
                        ready_msg = MIMEText(request.POST['message_send_in_bulk'])
                        ready_msg['subject']=request.POST['subject_send_in_bulk']
                        for ready_to_send in temp:
                            server.sendmail('geekydirect@gmail.com',str(ready_to_send),ready_msg.as_string())
                            count=count+1
                            print(count)
                        server.quit()
                        return render(request,'bulk_email_sender/emailsendsuccessfully.html',{'np':count})
                    except:
                        return render(request,'bulk_email_sender/somethingwentwrong.html',{})
                else:
                    return HttpResponse('we catch something went wrong in form validation pls contact admin')

            else:
                return HttpResponse("<h4 style='color:red;'>This application is for only admin</h4><p style='color:green;'>WE are currently working on this application to make generic</p>")
        else:
            return render(request,'bulk_email_sender/send_in_bulk.html',{'send_in_bulk_form':send_in_bulk_email()})

    else:
        return render(request,'bulk_email_sender/signinfirst.html',{})
