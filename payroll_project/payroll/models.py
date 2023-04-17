from django.db import models
from datetime import datetime
# Create your models here.


# Django model employee with salary
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)
    ideal_hours_per_day = models.IntegerField(default=8)

    def __str__(self):
        return self.name

    def total_attendance_hours(self):
        total_hours = 0
        for attendance in Attendance.objects.filter(employee=self):
            total_hours += attendance.total_hours()
        return total_hours

    # calculate total hours in range of dates
    def total_attendance_hours_in_range(self, start_date, end_date):
        total_hours = 0
        for attendance in Attendance.objects.filter(
            employee=self,
            date__range=[start_date, end_date]
        ):
            total_hours += attendance.total_hours()
        return total_hours

# Django model attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)

    def __str__(self):
        return self.employee.name + ', ' + str(self.date)
    
    # calculate the total hours worked
    def total_hours(self):
        time_in = datetime.combine(self.date, self.time_in)
        time_out = datetime.combine(self.date, self.time_out)
        time_temp = time_out - time_in
        # show only two decimal places
        return round(time_temp.seconds / 3600, 2)

    

# Django model salary
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    # Net deductions, <1 and calculated from total salary in a month
    net_deductions = models.DecimalField(max_digits=10, decimal_places=2)

    def total_salary(self):
        total = float(self.amount_per_hour * self.employee.total_attendance_hours())
        res = float(1-self.net_deductions) * float(total)
        return res

    # calculate total salary in range of dates
    def total_salary_in_range(self, start_date, end_date):
        total = float(self.amount_per_hour) * self.employee.total_attendance_hours_in_range(start_date, end_date)
        res = float(1-self.net_deductions) * (float(total))
        return res
















