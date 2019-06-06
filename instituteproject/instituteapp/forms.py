from .models import FeedbackData,ContactData
from django import forms
from multiselectfield import MultiSelectFormField

# from  instituteapp import views


class FeedbackForm(forms.Form):
    name=forms.CharField(
        label=' enter the name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'ente the name'
            }
        )
    )


    rating=forms.IntegerField(
        label=' enter the rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'ente the rating'
            }
        )
    )


    feedback=forms.CharField(
        label=' enter the feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'ente your feedback'
            }
        )
    )



#  Create Contact Data Form

class ContactForm(forms.Form):
    name=forms.CharField(
        label='Enter the Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )

    email=forms.EmailField(
        label='enter the email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email'
            }
        )
    )
    mobile=forms.IntegerField(
        label='enter your mobile',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number'
            }
        )
    )

    COURSES_CHOICES = (
        ('py', 'python'),
        ('dj', 'django'),
        ('ui', 'UI'),
        ('rest', 'RESTAPI')
    )

    courses =MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('mrg', 'morning'),
        ('aftrn', 'afternoon'),
        ('evng', 'evening'),
        ('night', 'night')
    )
    shifts = MultiSelectFormField(max_length=200, choices=SHIFTS_CHOICES)

    LOCATIONS_CHOICES = (
        ('hyd', 'hyderabad'),
        ('bang', 'banglaore'),
        ('chennai', 'chennai'),
        ('pune', 'pune')
    )
    locations = MultiSelectFormField(max_length=200, choices=LOCATIONS_CHOICES)

    GENDER_CHOICES=(
        ('m','male'),
        ('f','female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )

    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )




















