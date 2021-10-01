from django.http import request
from django.test import TestCase


# Create your tests here.
from .models import Student
import datetime
from django.urls import reverse

class StudentModelTestCase(TestCase):

    def setUp(self):
        self.student=Student(
            first_name="Akello",
            last_name="Olga Esther",
            age=20,
            phone_number="+256782899731",
            parent_name="Akello Agnes",
        ) 
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    def test_student_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_register_student_view(self):
        url=reverse("register_student")
        data={
            "first_name":self.student.first_name,
            "last_name":self.student.last_name,
            "age":self.student.age,
            "phone_number":self.student.phone_number,
            "parent_name":self.student.parent_name}

        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)    