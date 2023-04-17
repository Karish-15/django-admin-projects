from django import forms

from . import models

class InvitationForm(forms.ModelForm):
    class Meta:
        model = models.Invitation
        fields = ['receiver', 'group']

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender')
        super().__init__(*args, **kwargs)
        superusers = models.User.objects.filter(is_superuser=True)
        self.fields['receiver'].queryset = models.Employee.objects.exclude(name = self.sender.name)
        self.fields['group'].queryset = models.Group.objects.filter(members=self.sender)


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.sender = self.sender
        if commit:
            instance.save()
        return instance