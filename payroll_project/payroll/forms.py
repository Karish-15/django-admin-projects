from django import forms

from . import models

class AttendanceForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=models.Employee.objects.all())
    start_date = forms.DateField()
    end_date = forms.DateField()

class SalaryForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=models.Employee.objects.all())
    start_date = forms.DateField()
    end_date = forms.DateField()



