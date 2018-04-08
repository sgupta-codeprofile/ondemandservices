"""ondemandservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from start.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('start.urls')),
    path('auth/', include('social_django.urls', namespace='social')), #for social auth
    path('logout/',views.logout,name='logout'),
    path('bulk_email_sender/',include('bulk_email_sender.urls')),
    path('free_ebooks/',include('free_ebooks.urls')),
    path('image_resizer/',include('image_resizer.urls')),
    path('resume_maker/',include('resume_maker.urls')),
    path('start/',index ,name='home'),
    path('email_recorder/',include('email_recorder.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

