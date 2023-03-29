from django.db.models import Sum
from rest_framework import serializers

from staff.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):

    sum_salary_amount = serializers.SerializerMethodField()
    staff_number = serializers.SerializerMethodField()

    @staticmethod
    def get_sum_salary_amount(obj):
        return Employee.objects.filter(department=obj).aggregate(Sum('salary')).get('salary__sum')

    @staticmethod
    def get_staff_number(obj):
        return Employee.objects.filter(department=obj).count()

    class Meta:
        model = Department
        fields = [
            'title',
            'sum_salary_amount',
            'staff_number'
        ]


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'patrinimic',
            'foto',
            'position',
            'salary',
            'age',
            'department'
        ]
