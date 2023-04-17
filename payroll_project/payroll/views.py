from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Employee, Attendance, Salary

from . import forms

class EmployeeListView(ListView, LoginRequiredMixin):
    model = Employee
    template_name = 'home.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView, LoginRequiredMixin):
    model = Employee
    template_name = 'employee_detail.html'

class AttendanceView(View, LoginRequiredMixin):
    
    def get(self, request):
        form = forms.AttendanceForm()
        return render(request, 'attendance.html', {'form': form})

    def post(self, request):
        form = forms.AttendanceForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            attendances = Attendance.objects.filter(
                employee=employee,
                date__range=[start_date, end_date]
            )
            return render(request, 'attendance.html', {
                'form': form,
                'attendances': attendances,
                'total_hours': employee.total_attendance_hours_in_range(start_date, end_date),
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d')
            })
        return render(request, 'attendance.html', {'form': form})
        
class SalaryView(View, LoginRequiredMixin):
    
    def get(self, request):
        form = forms.SalaryForm()
        return render(request, 'salary.html', {'form': form})

    def post(self, request):
        form = forms.SalaryForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            salary = Salary.objects.get(employee=employee)
            return render(request, 'salary.html', {
                'form': form,
                'salary': salary,
                'total_salary': salary.total_salary_in_range(start_date, end_date)
            })
        return render(request, 'salary.html', {'form': form})

    
    


