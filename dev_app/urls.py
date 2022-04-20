from unicodedata import name
from django import views
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project'),
    path('create-project/',views.createProject,name="create-projects"),
    path('update-project/<str:pk>/',views.updateProject,name="update-project"),
    path('delate-project/<str:pk>/',views.delateProject,name="delate-project"),

]  