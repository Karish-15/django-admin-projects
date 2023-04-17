# Payroll System

A Django webapp to manage Attendance and Salary of Employees. Only admin can add employees, manage attendance and salary.


## Database

#### Employee



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Name of Employee|
| `email` | `string` | email of Employee|
| `phone` | `string` | Phone number of Employee |
| `address` | `string` | address of Employee |
| `date_hired` | `datetimefield` | Date on which Employee was hired |

#### Attendance



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `employee` | `ForeignKey` |ForeignKey to Employee model |
| `date` | `datefield` | Date of attendance|
| `time_in` | `timefield` | Entry time |
| `time_out` | `timefield` | Exit time |

#### Salary



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `employee` | `ForeignKey` | ForeignKey to Employee model |
| `amount_per_hour` | `DecimalField` | Salary to be paid per hour |
| `net_deductions` | `DecimalField` | Deductions (in %) to be done|



## Screenshots

![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/payroll_project/payroll_screenshots/Home.jpg)
![Form](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/payroll_project/payroll_screenshots/Form.jpg)
![Form](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/payroll_project/payroll_screenshots/attendance_list.jpg)
![Form](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/payroll_project/payroll_screenshots/salary.jpg)


