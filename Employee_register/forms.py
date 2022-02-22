from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields = ('Fullname','Mobile','emp_code','Position')
        labels={'Fullname':'Name',
                'emp_code':'Employee code',
                'Mobile':'Mobile number',
                'Position':'Job role'
                }