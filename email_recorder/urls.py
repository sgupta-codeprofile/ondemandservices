from django.urls import path
from email_recorder import views
app_name='email_recorder'

urlpatterns=[
    path('',views.index,name='index'),
    path('email_recorder/',views.downloadlist,name='download_list')




]