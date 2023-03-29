from django.contrib import admin

from staff.models import Department, Employee


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Full name', {'fields': ['first_name', 'last_name', 'patrinimic']}),
        ('Personal information', {'fields': ['age', 'foto']}),
        ('Employee information', {'fields': ['department', 'position', 'salary']})
    ]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
