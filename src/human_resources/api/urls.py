from django.urls import path
from . import views as _view

urlpatterns = [
    # * statics
    path('course-list/', _view.get_course, name='course-list'),
    path('faculty-list/', _view.get_faculty, name='faculty-list'),
    path('region-list/', _view.get_region, name='region-list'),
    path('parent-status-list/', _view.get_parent_status, name='parent-status-list'),
]