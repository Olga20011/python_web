from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=25,null=True)
    course_trainer=models.CharField(max_length=20,null=True)
    code=models.CharField(max_length=10,null=True)
    duration=models.PositiveSmallIntegerField(null=True)
    syllabus=models.TextField(null=True)
    

