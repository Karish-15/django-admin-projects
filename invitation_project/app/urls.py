from django.urls import path

from . import views

urlpatterns = [
    path('invitation_list/', views.InvitationListView.as_view(), name='invite_list'),
    path('invitation_detail/<int:pk>', views.InvitationDetailView.as_view(), name='invitation_detail'),
    path('invitation_accept/<int:pk>', views.InvitationAcceptView.as_view(), name='invitation_accept'),
    path('invitation_reject/<int:pk>', views.InvitationRejectView.as_view(), name='invitation_reject'),
    path('group_list/', views.GroupListView.as_view(), name='group_list'),
    path('group_detail/<int:pk>', views.GroupDetailView.as_view(), name='group_detail'),
    path('', views.HomeView.as_view(), name='home'),
    path('invitation_create/', views.InvitationcreateView.as_view(), name='invitation_create'),

]
