from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# manual serialiser here
# def studentsView(request):
#     students=Student.objects.all()
#     students_list=list(students.values())
#     print("students===>",students_list)
#     return JsonResponse(students_list,safe=False)



@api_view(['GET','POST'])
def studentsView(request):
    if request.method=='GET':
        students=Student.objects.all()
        serialiser=StudentSerializer(students,many=True)
        return Response(serialiser.data,status.HTTP_200_OK)
    if request.method=='POST':
        serialiser=StudentSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data,status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors,status.HTTP_400_BAD_REQUEST)