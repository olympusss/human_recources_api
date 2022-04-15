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