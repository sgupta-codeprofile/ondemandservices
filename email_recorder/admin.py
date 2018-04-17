from django.contrib import admin
from email_recorder.models import email,cat,liststore

# Register your models here.
admin.site.register(email)
admin.site.register(cat)
admin.site.register(liststore)