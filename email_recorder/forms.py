from django import forms


input_option=[
    ('Job_seekers','Job Seekers'),
    ('Earn_money','Earn Money'),
    ('Technology_lover','Technology'),
    ('Gadgets_lover','Gadgets lover'),
    ('Political','Political'),
    ('Crypto_currency','Crypto currency')


]
class catagories(forms.Form):
    cat_input=forms.CharField(label='Select Category',widget=forms.Select(choices=input_option,attrs={'class':'form-control'}))
    user_email=forms.EmailField(label='Enter Email',widget=forms.EmailInput(attrs={'class':'form-control'}))


input_option1=[
    ('Job_Seekers','Job Seekers'),
    ('Earn_Money','Earn Money'),
    ('Technology','Technology'),
    ('Gadgets_lover','Gadgets lover'),
    ('Political','Political'),
    ('Crypto_currency','Crypto currency')


]
class download_list(forms.Form):
    get_cat=forms.CharField(label='Select Category',widget=forms.Select(choices=input_option1,attrs={'class':'form-control'}))