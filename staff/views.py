from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from staff.models import Department, Employee
from staff.pagination import CustomPagination
from staff.serializers import DepartmentSerializer, EmployeeSerializer


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        last_name = self.request.query_params.get('last_name')
        if last_name:
            self.queryset = self.queryset.filter(last_name=last_name)

        depardment_id = self.request.query_params.get('dep_id')
        if depardment_id:
            self.queryset = self.queryset.filter(department_id=depardment_id)

        return self.queryset


class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all(),
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)


class EmployeeDetail(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)


class EmployeeDelete(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentList(ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
