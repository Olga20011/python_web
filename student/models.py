from django.db import models


# Create your models here.
class Student (models.Model):
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=12,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    # gender_choice=(
    #     ('1','Female'),
    #     ('2','Male'),
    #     ('3','Others'),
     
    # )
    # gender=models.CharField(max_length=15,choices=gender_choice,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    parent_name=models.CharField(max_length=12,null=True)
    parent_phone_number=models.CharField(max_length=15,null=True)
    date_of_birth=models.DateField(null=True)
    nationality_choice=(
        ('1','Ugandan'),
        ('2','Kenyan'),
        ('3','Rwandan'),
        ('4','South Sudanese'),
        ('5','Sudanese')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice,null=True)
    # student_roll_number=models.CharField(max_length=10,null=True)
    date_of_enrollment=models.DateField(null=True)
    # laptop_serial_number=models.CharField(max_length=5,blank=True,null=True)
    medical_report=models.FileField(upload_to="docs/",null=True)
    email_address=models.EmailField(max_length=50, null=True)
    profile=models.ImageField(upload_to="images/",null=True)
    national_id=models.CharField(max_length=12,null=True)
    county_or_district=models.CharField(max_length=12, null=True)
    languages_choice=(
        ('1','English'),
        ('2','French'),
        ('3','Kiswahili'),
        ('4','Kinyarwanda'),
        ('5','sudanese')
    )
    language=models.CharField(max_length=15,choices=languages_choice,null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    