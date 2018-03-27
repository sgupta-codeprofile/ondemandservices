from django import forms

class upload_image(forms.Form):
    width=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter the width',
                                                        'class':'form-control'
                                                        }))
    height=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter the height',
                                                        'class':'form-control'
                                                        }))
    image=forms.ImageField()