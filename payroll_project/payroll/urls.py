from django.urls import path

from . import views
urlpatterns = [
    
    path('', views.EmployeeListView.as_view(), name='home'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('attendance/', views.AttendanceView.as_view(), name='attendance'),
    path('salary/', views.SalaryView.as_view(), name='salary'),
    
]
