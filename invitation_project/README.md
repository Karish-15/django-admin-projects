# Invitation System 

A Django webapp to manage Employee details and Invite other employees to your groups. Only admin can add employees and create groups.


## Database

#### Employee



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Name of Employee|
| `email` | `string` | email of Employee|
| `phone` | `string` | Phone number of Employee |
| `position` | `ForeignKey` | ForeignKey to Position model |
| `date_hired` | `datetimefield` | Date on which Employee was hired |

#### Invitation



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sender` | `ForeignKey` |ForeignKey to Employee model |
| `receiver` | `ForeignKey` | ForeignKey to Employee model|
| `group` | `ForeignKey` | ForeignKey to Group model |
| `status` | `CharField` | pending, accepted or rejected |

#### Position



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `CharField` | Name of position |
| `level` | `DecimalField` | Numeric level, higher means superior |

#### Group



| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `CharField` | Name of Group |
| `members` | `ManyToManyField` | Contains Employee models which are part of the group |




## Screenshots

![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/invitation_project/invitation_screenshots/Home.jpg)
![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/main/invitation_project/invitation_screenshots/Create_invitation.jpg)
![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/invitation_project/invitation_screenshots/invitation_list.jpg)
![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/859e8a2d88a635d7ceb08bca47e110883bde6084/invitation_project/invitation_screenshots/group_list.jpg)
![Home](https://raw.githubusercontent.com/Karish-15/django-admin-projects/main/invitation_project/invitation_screenshots/Group_details.jpg)
