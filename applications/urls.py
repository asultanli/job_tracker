from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobApplicationListView.as_view(), name='application_list'),
    path('application/<int:pk>/', views.JobApplicationDetailView.as_view(), name='application_detail'),
    path('application/new/', views.JobApplicationCreateView.as_view(), name='application_create'),
    path('application/<int:pk>/edit/', views.JobApplicationUpdateView.as_view(), name='application_update'),
    path('application/<int:pk>/delete/', views.JobApplicationDeleteView.as_view(), name='application_delete'),
]