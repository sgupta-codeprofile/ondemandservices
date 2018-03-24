from django.db import models

# Create your models here.
class add_ebook(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/',default = 'no pic')



