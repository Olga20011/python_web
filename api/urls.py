
from django.db import router
from django.urls import include,path
from rest_framework import routers
from .views import StudentViewSet, TrainerViewSet,CoursesViewSet,EventsViewSet

router=routers.DefaultRouter()
router.register(r"students",StudentViewSet)
router.register(r"trainers",TrainerViewSet)
router.register(r"courses",CoursesViewSet)
router.register(r"calender",EventsViewSet)

urlpatterns=[
    path("",include(router.urls)),
]