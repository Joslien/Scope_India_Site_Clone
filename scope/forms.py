from django import forms
from django.forms import ModelForm
import re
from .models import contactdetails

gender=[('male','Male'),
        ('female','Female'),
        ('other','Other')]
courses=[
         ('Choose your courses','hoose your course!'),
         ('Data Science & AI Course','Data Science & AI Course'),
         ('Data Analytics Course','Data Analytics Course')
]
mode=[
      ('live online','Live online'),
      ('classrom','Classroom')
]
loc=[
     ('technopark tvm','Technopark TVM'),
     ('thampanoor tvm','Thampanoor TVM'),
     ('kochi','Kochi'),
     ('nagercoil','Nagercoil'),
     ('online','Online')
]
timimg=[
     ('8-10am', 'Between 8am - 10am'),
     ('9-1pm', 'Between 9am - 1pm'),
     ('1-6pm', 'Between 1pm - 6pm'),
     ('6-10pm', 'Between 6pm - 10pm'),
]
hobbies=[
    ('singing','Singing'),
    ('dancing','Dancing'),
    ('drawing','Drawing'),
    ('reading','Reading'),
    ('gaming','Gaming')
]


class registrform(forms.Form):
    fullname=forms.CharField(required=True)
    dob=forms.DateField(
        widget=forms.DateInput(
        attrs={
            'type': 'date',
            'placeholder': 'dd-mm-yyyy'
        }),
        required=True)
    gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect(attrs={'class': 'gender-inline'}))
    qualification=forms.CharField()
    number=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    guardian=forms.CharField()
    occupation=forms.CharField()
    mobile=forms.CharField()
    course=forms.ChoiceField(choices=courses)
    loc=forms.ChoiceField(choices=loc,widget=forms.RadioSelect,required=True)
    Mode=forms.ChoiceField(choices=mode,widget=forms.RadioSelect,required=True)
    # time = forms.ChoiceField(choices=timimg,widget=forms.CheckboxSelectMultiple,required=True)
    time = forms.MultipleChoiceField(choices=timimg, widget=forms.CheckboxSelectMultiple, required=True)
    hobby = forms.MultipleChoiceField(choices=hobbies, widget=forms.CheckboxSelectMultiple, required=True)
    Address=forms.CharField()
    country=forms.CharField(required=True)
    state=forms.CharField(required=True)
    city=forms.CharField(required=True)
    pin=forms.CharField()
    files=forms.FileField(required=True)

    def clean_number(self):
        value=self.cleaned_data['number']
        pattern=r'^[0-9]{10}$'
        if not re.match(pattern,str(value)):
             raise forms.ValidationError("Not Valid Phone Number")
        else:
            return value
    
    def clean_email(self):
        value=self.cleaned_data['email']
        pattern=r'^[a-zA-Z0-9]+@gmail\.com$'
        if not re.match(pattern,value):
             raise forms.ValidationError("Not email pattern")
        else:
            return value
    
    def clean_mobile(self):
        value=self.cleaned_data['mobile']
        pattern=r'^[0-9]{10}$'
        if not re.match(pattern,str(value)):
             raise forms.ValidationError("Not Valid Phone Number")
        else:
            return value
        


# class contactform(forms.ModelForm):
#     class Meta:
#         model=contactdetails
#         fields='__all__'

    