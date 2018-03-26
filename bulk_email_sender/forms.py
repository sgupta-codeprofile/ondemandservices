from django import forms

class Sendmail(forms.Form):
    reciver=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'TO',
                                                                        'class':'form-control'
                                                                        }))
    subject=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter subject',
                                                                        'class':'form-control'
                                                                        }))
    message=forms.CharField(widget=forms.Textarea(attrs={'width':"50%", 'cols' : "70", 'rows': "10",
                                                         'placeholder': 'Enter subject',
                                                         'class': 'form-control'
                                                         }))



class user_email_list(forms.Form):
    add_email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter email to add our database',
                                                              'class':'form-control'

                                                              }))

class send_in_bulk_email(forms.Form):

    subject_send_in_bulk=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter subject',
                                                                        'class':'form-control'
                                                                        }))
    message_send_in_bulk=forms.CharField(widget=forms.Textarea(attrs={'width':"50%", 'cols' : "70", 'rows': "10",
                                                         'placeholder': 'Enter subject',
                                                         'class': 'form-control'
                                                         }))