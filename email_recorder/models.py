from django.db import models


class email(models.Model):
    usr_email=models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        return self.usr_email


class cat(models.Model):
    email=models.ForeignKey(email,on_delete=models.CASCADE)
    test=models.CharField(max_length=100,default='none by user')

    def __str__(self):
        return self.test


class liststore(models.Model):
    cat=models.ForeignKey(cat,on_delete=models.CASCADE)
    heavylist=models.CharField(max_length=100,default='none by admin')

    def __str__(self):
        return self.heavylist


