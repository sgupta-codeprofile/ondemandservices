from django.urls import path
from . import views
app_name='free_ebooks'
urlpatterns=[

    path('',views.index,name='index'),
    path('add_ebooks1/',views.add_ebooks,name='add_ebooks1')
]