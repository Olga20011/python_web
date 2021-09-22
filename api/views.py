from django.shortcuts import render

from .serializers import StudentSerializer,TrainerSerializer,CoursesSerializer,EventsSerializer
from rest_framework import serializers,viewsets
from student.models import Student
from trainer .models import Trainer
from courses.models import Courses
from calender.models import Events

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventsSerializer            