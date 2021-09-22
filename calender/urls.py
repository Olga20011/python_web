from django.urls import path
from .views import CalendarView, event, register_calender,calendar_profile,edit_calender

urlpatterns=[
    path("register/",register_calender,name="register_calender"),
    path("list/",CalendarView.as_view(),name="CalenderView"),
    path("events/",event,name="events"),
    path("profile/<int:id>/",calendar_profile,name="calender_profile"),
    path("edit/<int:id>/",edit_calender,name="edit_calender")

]