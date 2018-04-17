from django import forms


input_option=[
    ('first','Job Seeker'),
    ('second','Eearn Money'),


]
class catagories(forms.Form):
    cat_input=forms.CharField(label='Select Category',widget=forms.Select(choices=input_option,attrs={'class':'form-control'}))
    user_email=forms.EmailField(label='Enter Email',widget=forms.EmailInput(attrs={'class':'form-control'}))


class download_list(forms.Form):
    get_cat=forms.CharField(label='Select Category',widget=forms.Select(choices=input_option,attrs={'class':'form-control'}))