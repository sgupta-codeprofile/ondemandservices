from  django import forms
from .models import add_ebook

class input_ebook_detail(forms.Form):
      title_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter title','class':'form-control',}))
      ebook_description=forms.CharField(max_length=500,widget=forms.TextInput(attrs={'placeholder': 'Enter Description','class': 'form-control',}))
      input_image=forms.ImageField()
      input_ebook=forms.FileField()






