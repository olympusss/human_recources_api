from django.db import models

# Create your models here.

class Courses(models.Model):
    name        = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'courses'
        

class Faculties(models.Model):
    name        = models.CharField(max_length=50)
    dean_id     = models.IntegerField(default=1)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'faculties'
        
        
class Regions(models.Model):
    name        = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'regions'
        
        
class ParentStatus(models.Model):
    name        = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'parent_status' 
        
        
class Students(models.Model):
    name                    = models.CharField(max_length=50)
    surname                 = models.CharField(max_length=50)
    father_name             = models.CharField(max_length=50)
    identification_number   = models.IntegerField()
    course_id               = models.ForeignKey(Courses, related_name='course', on_delete=models.CASCADE)
    faculty_id              = models.ForeignKey(Faculties, related_name='faculty', on_delete=models.CASCADE)
    klass                   = models.CharField(max_length=50)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'students'