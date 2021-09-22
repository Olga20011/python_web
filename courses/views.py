from .models import Courses
from django.shortcuts import render,redirect
from.forms import CoursesRegistrationForm

# Create your views here.
def register_courses(request):
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{"form":form})

def courses_list(request):
    course=Courses.objects.all()
    return render(request,"courses_list.html",{"course":course})   

def courses_profile(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"courses_profile.html",{"courses":courses})

def edit_courses(request,id):
    courses=Courses.objects.get(id=id)
    if request.method=="POST":
        form=CoursesRegistrationForm(request.Post,instance=courses)
        if form.is_valid():
            form.save    
            return  redirect("courses_profile",id=courses.id)
    else:
        form=CoursesRegistrationForm(instance=courses) 
        return render(request,"edit_courses.html",{"form":form})      






