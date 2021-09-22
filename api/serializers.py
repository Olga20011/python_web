from rest_framework import fields, serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from calender.models import Events

class StudentSerializer(serializers.ModelSerializer):

   class Meta:
    model=Student
    fields=("first_name","last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
   class Meta:
      model=Trainer
      fields="__all__"

class CoursesSerializer(serializers.ModelSerializer):
   class Meta:
      model=Courses
      fields="__all__"

class EventsSerializer(serializers.ModelSerializer):
   class Meta:
      model=Events
      fields="__all__"                  