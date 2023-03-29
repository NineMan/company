from django.db import models

from staff.utils import choices_max_length


class Department(models.Model):
    """Отделы."""

    title = models.CharField('Title', max_length=80)

    def __str__(self):
        return self.title

    @property
    def head_of_department(self):
        return Employee.objects.filter(department=self, position=Employee.HEAD_OF_DEPARTMENT).first()


class Employee(models.Model):
    """Сотрудники."""

    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    HEAD_OF_DEPARTMENT = 'head_of_department'
    POSITION_CHOICES = [
        (EMPLOYEE, 'Сотрудник'),
        (MANAGER, 'Менеджер'),
        (HEAD_OF_DEPARTMENT, 'Руководитель отдела'),
    ]
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, db_index=True)
    patrinimic = models.CharField(max_length=128)
    foto = models.ImageField(upload_to='./foto')
    position = models.CharField(
        max_length=choices_max_length(POSITION_CHOICES),
        choices=POSITION_CHOICES,
    )
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
