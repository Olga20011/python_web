from django.db import models

# Create your models here.
class Student (models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    studentRollNumber=models.CharField(max_length=10)
    date_of_enrollment=models.DateField()
    laptop_serial_number=models.CharField(max_length=5)
    health_status=models.FileField()
    email_address=models.EmailField()
    profile=models.ImageField()
    Class=models.CharField(max_length=8)
    nationalId=models.CharField(max_length=12)
    countyORdistrict=models.CharField(max_length=12)
    
    


    