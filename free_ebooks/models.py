from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.
class add_ebook(models.Model):
    user_name=models.CharField(max_length=50,default='anaonymous_user')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/',default = 'no pic')
    ebook_download=models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT),
                                    upload_to='media/', default='no file')



