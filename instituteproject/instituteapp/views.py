from django.shortcuts import render
from.models import FeedbackData,ContactData,CoursesData
from .forms import FeedbackForm,ContactForm
from django.http import HttpResponse
import  datetime
date1=datetime.datetime.now()

def main_page(request):
    return  render(request,'Base.html')


def home_page(request):
    return render(request,'home.html')



#if we want to select multiple fileds at a time and store in the database .."use Cleaned_data.get()"

def contact_page(request):

    if request.method == "POST":

        cform=ContactForm(request.POST)

        if cform.is_valid():

            name=cform.cleaned_data.get('name')
            email = cform.cleaned_data.get('email')
            mobile = cform.cleaned_data.get('mobile')
            courses = cform.cleaned_data.get('courses')
            shifts= cform.cleaned_data.get('shifts')
            locations = cform.cleaned_data.get('locations')
            gender = cform.cleaned_data.get('gender')
            start_date = cform.cleaned_data.get('start_date')


            data=ContactData(

                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shifts=shifts,
                locations=locations,
                gender=gender,
                start_date=start_date
                )
            data.save()
            cform=ContactForm()

            return render(request,'contact.html',{'cform':cform})
        else:
            return HttpResponse('user invalid data')
    else:
         cform=ContactForm()
         return render(request,'contact.html',{'cform':cform})


# course_page view code

def course_page(request):
    courses=CoursesData.objects.all()
    return render(request,'course.html',{'courses':courses})




def ourteam_page(request):
    return render(request,'ourteam.html')

def gallery_page(request):
    return render(request,'gallery.html')

def feedback_page(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            fdata=FeedbackData.objects.all()
            return render(request, 'feedback.html', {'fform': fform,'fdata':fdata})
        else:
            return HttpResponse('Invalid User data')


    else:
        fform=FeedbackForm()
        fdata=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})












# this code is Rajareddy

# def feedback_page(request):
#     if request.method =='POST':
#         fform=FeedbackForm(request.POST)
#         if fform.is_valid():
#             name=request.POST.get('name')
#             rating=request.POST.get('rating')
#             feedback=request.POST.get('feedback')
#             data=FeedbackData(
#                 name=name,
#                 rating=rating,
#                 feedback=feedback
#             )
#             data.save()
#             fform=FeedbackForm()
#             fdata=FeedbackData.objects.all()
#             return render(request,'feedback.html',{'fform':fform},{'fdata':fdata})
#         else:
#             return HttpResponse('invalid user data')
#     else:
#
#         fform = FeedbackForm()
#         fdata=FeedbackData.objects.all()
#         return render(request,'feedback.html',{'fform':fform},{'fdata':fdata})