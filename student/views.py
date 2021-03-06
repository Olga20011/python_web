from django.db.models.fields import CommaSeparatedIntegerField
from django.http import request
from .models import Student
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForms


def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForms(request.POST or None,request.FILES)
        if form.is_valid():
            form.save(commit=False)
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForms()
    return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})  

def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":student})

def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentRegistrationForms(request.Post,instance=student)
        if form.is_valid():
            form.save    
            return  redirect("student_profile",id=student.id)
    else:
        form=StudentRegistrationForms(instance=student) 
        return render(request,"edit_student.html",{"form":form})      


