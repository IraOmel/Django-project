from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('projects', views.projects, name='projects'),
    path('cooperation', views.emp_form, name='cooperation'),
    path('project/<str:name>', views.one_project, name='one_project'),
]
