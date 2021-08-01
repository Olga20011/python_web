from django.shortcuts import render
from .forms import StudentRegistrationForms


def register_student(request):
    form=StudentRegistrationForms()
    return render(request,"register_student.html",{"form":form})

