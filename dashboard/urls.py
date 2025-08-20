from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('teams/', views.teams_list, name='teams_list'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('teams/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('kpis/', views.kpis_list, name='kpis_list'),
    path('kpis/<int:pk>/', views.kpi_detail, name='kpi_detail'),
    path('kpis/<int:pk>/edit/', views.kpi_edit, name='kpi_edit'),
    path('kpis/<int:pk>/delete/', views.kpi_delete, name='kpi_delete'),
    path('bpos/', views.bpos_list, name='bpos_list'),
    path('bpos/<int:pk>/', views.bpo_detail, name='bpo_detail'),
    path('bpos/<int:pk>/edit/', views.bpo_edit, name='bpo_edit'),
    path('bpos/<int:pk>/delete/', views.bpo_delete, name='bpo_delete'),
    path('about/', views.about, name='about'),
]
