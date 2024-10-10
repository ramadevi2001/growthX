# assignments/urls.py

from django.urls import path
from .views import (
    UploadAssignmentView,
    AdminAssignmentListView,
    accept_assignment,
    reject_assignment,
    AllAdminsView,
)

urlpatterns = [
    path('upload/', UploadAssignmentView.as_view(), name='upload-assignment'),
    path('assignments/', AdminAssignmentListView.as_view(), name='admin-assignments'),
    path('assignments/<str:pk>/accept/', accept_assignment, name='accept-assignment'),
    path('assignments/<str:pk>/reject/', reject_assignment, name='reject-assignment'),
    path('all-admins/', AllAdminsView.as_view(), name='all-admins'),
]