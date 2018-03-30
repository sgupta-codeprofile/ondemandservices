from  django import forms

carrer_object=[
    ('first','To be involve in work, where I can utilize my programming skill and other skill to develop and manage the projects. And I also want to make a sound position in corporate world and work enthusiastically in team to achieve goal of the organization/MNC with devotion and hard work.'),
    ('second','I want a highly rewarding career where I can use my skills and knowledge to help the company and my coworkers be successful'),
    ('third','I am seeking a company where I can use my experience and education to help the company meet and surpass its goals.'),
    ('fourth','o work in a highly competitive environment with a perfect challenge by contributing the best for  the growth of the organization while ensuring growth in personal career'),
    ('fifth','To Be a Successful professional in a Globally Respected Company and to achieve the objectives of the company with Honesty and Fairness and to Continuously Upgrade My Knowledge and Skills.'),
    ('sixth','Looking for opportunities to build my carrier that would help me in achieving greater practical excellence in software industry, exceptional with hardworking nature along with good communication skill to explore the requirements and come up with innovative solution'),
    ('seventh','To work in a Challenging environment where I can put my best efforts and knowledge to reach the respective company’s goals and objectives.'),
    ('eighth','To work in a progressive organization where I can enhance my skills and learning to contribute to the success of the organization'),
    ('ninth','As a Beginner in the Industrial field, while making a  positive  contribution, I would like to build a career, making the best use of my analytical, creative and logical skills to perform the job efficiently'),
    ('tenth','To work in a challenging environment where I can prove my capabilities through hard work and team play.'),
]

class Resume(forms.Form):
    first_name=forms.CharField(label='First name:',max_length=100,widget=forms.TextInput(attrs={'placeholder':'First name',
                                                                            'class':'form-control'
                                                                            }))
    last_name=forms.CharField(label='Last name:',max_length=100,widget=forms.TextInput(attrs={'placeholder':'First name',
                                                                            'class':'form-control'
                                                                            }))
    carrer_objectives=forms.CharField(label='Select carrer object',widget=forms.Select(choices=carrer_object,attrs={'class':'form-control'}))
    #technical skills
    technical_skills1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Technical skills ex-c,c++,python etc',
                                                                            'class':'form-control'
                                                                            }))
    technical_skills2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name',
                                                                      'class': 'form-control'
                                                                      }))
    technical_skills3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name',
                                                                      'class': 'form-control'
                                                                      }))
    technical_skills4 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name',
                                                                      'class': 'form-control'
                                                                      }))
    technical_skills5 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name',
                                                                      'class': 'form-control'
                                                                      }))
    #Education
    college1= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Course: EX-BE/BTECH',
                                                                      'class': 'form-control'
                                                                      }))
    institute1 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Institute/College name',
                                                                      'class': 'form-control'
                                                                      }))
    university1 = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'University name',
                                                                      'class': 'form-control'
                                                                      }))


    Score1 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter percentage %',
                                                                      'class': 'form-control'
                                                                      }))
    #Education 2
    college2= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Course-> EX-SSC[class-12]',
                                                                      'class': 'form-control'
                                                                      }))
    institute2 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter school name',
                                                                      'class': 'form-control'
                                                                      }))
    university2 = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Board Ex-ISC/CBSE',
                                                                      'class': 'form-control'
                                                                      }))


    Score2 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter percentage %',
                                                                      'class': 'form-control'
                                                                      }))
    #Education 3
    college3= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Course-> EX-HSC[class 10]',
                                                                      'class': 'form-control'
                                                                      }))
    institute3 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter school name',
                                                                      'class': 'form-control'
                                                                      }))
    university3 = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Board Ex-ISC/CBSE',
                                                                      'class': 'form-control'
                                                                      }))


    Score3= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter percentage %',
                                                                      'class': 'form-control'
                                                                      }))


