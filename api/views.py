from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from employees.models import Employee
from students.models import Student
from . serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics


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



#GET, PUT, DELETE
@api_view(['GET','PUT','DELETE'])
def studentsDetailView(request,pk):
    student=get_object_or_404(Student,id=pk)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status.HTTP_200_OK)
    if request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        student.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# APIView type

# class Employees(APIView):
#     def get(self,request):
#         students=Employee.objects.all()
#         serializer=EmployeeSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)



# class EmployeesDetail(APIView):
#     def get_object(self,pk):
#         return get_object_or_404(Employee,id=pk)
    
#     def get(self,request,pk):
#         employee=self.get_object(pk)

#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employee=self.get_object(pk)

#         serializer=EmployeeSerializer(employee,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        


#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# Mixins 

class Employees(mixins.ListModelMixin,mixins.CreateModelMixin ,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeesDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)