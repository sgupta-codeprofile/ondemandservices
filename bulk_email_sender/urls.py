from django.urls import path
from . import views
app_name='bulk_email_sender'

urlpatterns=[

    path('',views.index, name='index'),


]