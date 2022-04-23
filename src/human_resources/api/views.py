from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models as _mod
from . import serializers as _ser
import json
from .returns import Returns

# Create your views here.

BASE_PATH_TO_JSON = 'D:\\Project\\human_recources_api\\src\\json\\'

@api_view(['GET'])
def get_course(request):
    courses = _mod.Courses.objects.all()
    serializer = _ser.CourseSerializer(courses, many=True)
    if serializer.data:
        return Response(serializer.data)
    f = open(BASE_PATH_TO_JSON + 'courses.json')
    data = json.load(f)
    for i in data:
        name = i.get('name')
        serializer = _ser.CourseSerializer(data={
            'name' : name
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(Returns.NOT_INSERTED)
    courses = _mod.Courses.objects.all()
    serializer = _ser.CourseSerializer(courses, many=True)
    if serializer.data:
        return Response(serializer.data)



@api_view(['GET'])
def get_faculty(request):
    faculties = _mod.Faculties.objects.all()
    serializer = _ser.FacultySerializer(faculties, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    f = open(BASE_PATH_TO_JSON + 'fakultetler.json')
    data = json.load(f)
    for i in data:
        name = i.get('name')
        serializer = _ser.FacultySerializer(data={
            'name': name
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(Returns.NOT_INSERTED)
    faculties = _mod.Faculties.objects.all()
    serializer = _ser.FacultySerializer(faculties, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    
    
@api_view(['GET'])
def get_region(request):
    regions = _mod.Regions.objects.all()
    serializer = _ser.RegionSerializer(regions, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    f = open(BASE_PATH_TO_JSON + 'welayatlar.json')
    data = json.load(f)
    for i in data:
        name = i.get('name')
        serializer = _ser.RegionSerializer(data={
            'name': name
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(Returns.NOT_INSERTED)
    regions = _mod.Regions.objects.all()
    serializer = _ser.RegionSerializer(regions, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    
    
@api_view(['GET'])
def get_parent_status(request):
    parent = _mod.ParentStatus.objects.all()
    serializer = _ser.ParentStatusSerializer(parent, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    f = open(BASE_PATH_TO_JSON + 'parent_status.json')
    data = json.load(f)
    for i in data:
        name = i.get('name')
        serializer = _ser.ParentStatusSerializer(data={
            'name' : name
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(Returns.NOT_INSERTED)
    parent = _mod.ParentStatus.objects.all()
    serializer = _ser.ParentStatusSerializer(parent, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    
    
@api_view(['GET'])
def get_students(request):
    students = _mod.Students.objects.all()
    serializer = _ser.StudentSerializer(students, many=True)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    else:
        return Response(Returns.NULL)
    
    
@api_view(['POST'])
def add_student(request):
    serializer = _ser.StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_current_student(request):
    id = request.query_params.get('id', None)
    student = _mod.Students.objects.get(id=id)
    serializer = _ser.StudentSerializer(student)
    if serializer.data:
        return Response(Returns.object(serializer.data))
    else:
        return Response(Returns.STUDENT_NOT_FOUND)


@api_view(['PUT'])
def update_student(request):
    id = request.query_params.get('id', None)
    req = request.data
    student = _mod.Students.objects.get(id=id)
    print(req)
    serializer = _ser.StudentSerializer(
        instance=student, 
        data = {
            "name"                  : req["name"],
            "surname"               : req["surname"],
            "father_name"           : req["father_name"],
            "identification_number" : req["identification_number"],
            "course_id"             : req["course_id"],
            "faculty_id"            : req["faculty_id"],
            "klass"                 : req["klass"],
        }
    )
    if serializer.is_valid():
        serializer.save()
    return Response(Returns.UPDATED)


@api_view(['DELETE'])
def delete_student(request):
    id = request.query_params.get('id', None)
    student = _mod.Students.objects.get(id=id)
    student.delete()
    return Response(Returns.DELETED)