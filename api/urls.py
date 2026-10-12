from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeesViewset) # basename='employee' needed for ViewSet only
urlpatterns = [
    path('students/',views.studentsView, name='studentsView'), #GET,POST
    path('students/<int:pk>/',views.studentsDetailView, name='studentsDetailView'), #GET,PUT,DELETE

    # class based views and generics and mixins are needed for this type of url routing 
#     path('employees/',views.Employees.as_view()),

#     path('employees/<int:pk>/',views.EmployeesDetail.as_view()),

    # for viewSet needed routers 
    path('',include(router.urls))
]