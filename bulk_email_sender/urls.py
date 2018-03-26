from django.urls import path
from . import views
app_name='bulk_email_sender'

urlpatterns=[

    path('',views.index, name='index'),
    path('add_email/',views.add_email,name='add_email'),
    path('send_in_bulk/',views.send_in_bulk,name='send_in_bulk'),


]