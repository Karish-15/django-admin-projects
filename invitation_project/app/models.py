from django.db import models

# Create your models here.
from django.contrib.auth.models import User


#django model for employee position
class Position(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.name


#Django model for employees
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name + ", " + self.position.name)

#Django model for group in organization
class Group(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Employee, null=True, blank=True)

    def __str__(self):
        return self.name

# django model for invitations
class Invitation(models.Model):
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')), default='pending')

    def __str__(self):
        return (self.sender.name + " invited " + self.receiver.name + " to " + self.group.name)

    def accept(self):
        self.status = 'accepted'
        self.group.members.add(self.receiver)
        self.save()

    def reject(self):
        self.status = 'rejected'
        self.delete()



