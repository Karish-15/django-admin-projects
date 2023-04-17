from django.shortcuts import render

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from . import forms


from . import models

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class InvitationListView(ListView, LoginRequiredMixin):
    model = models.Invitation
    template_name = 'invitation_list.html'
    context_object_name = 'invitation'

    def get_queryset(self):
        receiver = models.Employee.objects.get(user=self.request.user)
        object_list = models.Invitation.objects.filter(receiver=receiver).filter(status='pending')
        # exclude invitations for groups that the user is already a member of
        for invitation in object_list:
            if receiver in invitation.group.members.all():
                object_list = object_list.exclude(pk=invitation.pk)
                # delete invitation if user is already a member of the group
                instance = models.Invitation.objects.get(pk=invitation.pk)
                instance.delete()
        
        return object_list

class InvitationcreateView(CreateView, LoginRequiredMixin):
    model = models.Invitation
    form_class = forms.InvitationForm
    template_name = 'invitation_create.html'

    def get_success_url(self):
        return reverse('invite_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['sender'] = models.Employee.objects.get(user=self.request.user)
        return kwargs

    # function to destroy invitation if user is already a member of the group
    def form_valid(self, form):
        invitation = form.save(commit=False)
        invitation.save()
        if invitation.receiver in invitation.group.members.all():
            invitation.delete()
        
        return redirect('invite_list')


class GroupListView(ListView, LoginRequiredMixin):
    model = models.Group
    template_name = 'group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        employee = models.Employee.objects.get(user=self.request.user)
        object_list = models.Group.objects.filter(members=employee)
        return object_list

class GroupDetailView(DetailView, LoginRequiredMixin):
    model = models.Group
    template_name = 'group_detail.html'
    
    
    

class InvitationDetailView(DetailView, LoginRequiredMixin):
    model = models.Invitation
    template_name = 'invitation_detail.html'

class InvitationAcceptView(View, LoginRequiredMixin):
    def get(self, request, pk):
        invitation = models.Invitation.objects.get(pk=pk)
        context = {'invitation': invitation}
        return render(request, 'invitation_accept.html', context)

    def post(self, request, pk):
        invitation = models.Invitation.objects.get(pk=pk)
        if (request.user == invitation.receiver.user):
            invitation.accept()
        return redirect('invite_list')

class InvitationRejectView(View, LoginRequiredMixin):
    def get(self, request, pk):
        invitation = models.Invitation.objects.get(pk=pk)
        context = {'invitation': invitation}
        return render(request, 'invitation_reject.html', context)

    def post(self, request, pk):
        invitation = models.Invitation.objects.get(pk=pk)
        if (request.user == invitation.receiver.user):
            invitation.reject()
        return redirect('invite_list')





