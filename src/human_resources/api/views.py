from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Courses
from .serializers import CourseSerializer

# Create your views here.

@api_view(['GET'])
def get_course(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    if serializer.data:
        return Response(serializer.data)


@api_view(['POST'])
def add_course(request):
    name = request.data.get('name')
    serializer = CourseSerializer(data={
        'name' : name
    })
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
