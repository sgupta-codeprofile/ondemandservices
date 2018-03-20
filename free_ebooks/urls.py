from django.urls import path
from . import views
app_name='free_ebooks'
urlpatterns=[

    path('',views.index,name='index'),
    path('add_ebooks/',views.add_ebooks,name='add_ebooks')
]