from django.db import models


# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
    )
    gender=models.CharField(max_length=10,choices=gender_choice,null=True)
    bio=models.TextField(null=True)
    courses_trained=models.CharField(max_length=30,null=True)
    email_address=models.EmailField(max_length=30,null=True)
    profile=models.ImageField(upload_to="images/", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
   
    

