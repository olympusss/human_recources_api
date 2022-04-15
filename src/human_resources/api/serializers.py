from rest_framework import serializers
from .models import Courses

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'created_at', 'updated_at']