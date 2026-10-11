from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentsView, name='studentsView'), #GET,POST
    path('students/<int:pk>/',views.studentsDetailView, name='studentsDetailView'), #GET,PUT,DELETE


    path('employees/',views.Employees.as_view()),

    path('employees/<int:pk>/',views.EmployeesDetail.as_view()),
]