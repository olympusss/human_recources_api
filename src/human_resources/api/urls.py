from django.urls import path
from . import views as _view

urlpatterns = [
    # * statics
    path('course-list/', _view.get_course, name='course-list'),
    path('faculty-list/', _view.get_faculty, name='faculty-list'),
    path('region-list/', _view.get_region, name='region-list'),
    path('parent-status-list/', _view.get_parent_status, name='parent-status-list'),
    
    # * students
    path('student-list/', _view.get_students, name='student-list'),
    path('student-get-current/', _view.get_current_student, name='student-get-current'),
    path('student-add/', _view.add_student, name='student-add'),
    path('student-update/', _view.update_student, name='student-update'),
    path('student-delete/', _view.delete_student, name='student-delete'),
]