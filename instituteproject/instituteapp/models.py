from django.db import models

from multiselectfield import MultiSelectField

class FeedbackData(models.Model):
    name=models.CharField(max_length=30)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=50)
    date=models.DateTimeField()



# createa a model for Contact Page

class ContactData(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    mobile=models.BigIntegerField()


    COURSES_CHOICES=(
        ('py','python'),
        ('dj','django'),
        ('ui','UI'),
        ('rest','RESTAPI')
    )

    courses=MultiSelectField(max_length=200,choices=COURSES_CHOICES)

    SHIFTS_CHOICES=(
        ('mrg','morning'),
        ('aftrn','afternoon'),
        ('evng','evening'),
        ('night','night')
    )
    shifts=MultiSelectField(max_length=200,choices=SHIFTS_CHOICES)

    LOCATIONS_CHOICES=(
        ('hyd','hyderabad'),
        ('bang','banglaore'),
        ('chennai','chennai'),
        ('pune','pune')
    )
    locations=MultiSelectField(max_length=200,choices=LOCATIONS_CHOICES)

    gender=models.CharField(max_length=50)
    start_date=models.DateField(max_length=100)

# createa a model for courses page

class CoursesData(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=200)
    course_dur=models.IntegerField()
    course_fee=models.IntegerField()
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()













