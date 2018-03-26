from django.contrib import admin
from bulk_email_sender.models import Maildata,email_list,Maildata_send_in_bulk

# Register your models here.
admin.site.register(Maildata)
admin.site.register(email_list)
admin.site.register(Maildata_send_in_bulk)