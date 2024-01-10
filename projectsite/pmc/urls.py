from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contractor.html', views.contractor_view, name='contractor'),
    path('project.html', views.project_view, name='project'),
    path('experience.html', views.experience_view, name='experience'),
    path('skill.html', views.skill_view, name='skill'),
]
