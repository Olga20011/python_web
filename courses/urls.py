
from django.urls import path
from .views import edit_courses, register_courses,courses_list,courses_profile

urlpatterns=[
    path("register/",register_courses,name="register_courses"),
    path("list/",courses_list,name="courses_list"),
    path("profile/<int:id>/",courses_profile,name="courses_profile"),
    path("edit/<int:id>/",edit_courses,name="edit_courses")

]