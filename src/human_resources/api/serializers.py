from rest_framework import serializers
from . import models as _mod

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = _mod.Courses
        fields = ['id', 'name', 'created_at', 'updated_at']
        

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = _mod.Faculties
        fields = ['id', 'name', 'created_at', 'updated_at']
        
        
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = _mod.Regions
        fields = ['id', 'name', 'created_at', 'updated_at']
        
        
class ParentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = _mod.ParentStatus
        fields = ['id', 'name', 'created_at', 'updated_at']