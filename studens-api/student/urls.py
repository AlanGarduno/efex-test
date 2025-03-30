from rest_framework.routers import DefaultRouter
from student.views import StudentViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('student', StudentViewSet)

app_name = 'student'

urlpatterns = [
    path('', include(router.urls))
]
