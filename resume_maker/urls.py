from django.urls import path
from . import views
app_name='resume_maker'
urlpatterns=[

    path('',views.index,name="index"),

]