from django.urls import path
from . import views

urlpatterns = [
    path('course-list/', views.get_course, name='course-list'),
    path('course-add/', views.add_course, name='course-list')
]