from django.db import models

# Create your models here.
class Maildata(models.Model):
    sender_data=models.CharField(max_length=50)
    reciver_data=models.CharField(max_length=50)
    subject_data=models.CharField(max_length=50)
    message_data=models.CharField(max_length=100)


class email_list(models.Model):
    userlist=models.EmailField()


    def __str__(self):
        return self.userlist

class Maildata_send_in_bulk(models.Model):
    sender_data_send_in_bulk=models.CharField(max_length=50)
    reciver_data_send_in_bulk=models.CharField(max_length=50)
    subject_data_send_in_bulk=models.CharField(max_length=50)
    message_data_send_in_bulk=models.CharField(max_length=100)