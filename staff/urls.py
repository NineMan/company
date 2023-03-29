from django.urls import path

from staff.views import (
    DepartmentList,
    EmployeeCreate,
    EmployeeDelete,
    EmployeeDetail,
    EmployeeList,
)

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='retrieve-employee'),
    path('employee/create/', EmployeeCreate.as_view(), name='create-employee'),
    path('employee/delete/<int:pk>/', EmployeeDelete.as_view(), name='delete-employee'),

    path('department/', DepartmentList.as_view()),
]
