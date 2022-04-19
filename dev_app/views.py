from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tag,Review




def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'projects.html',context)


def project(request,pk):
    project = Project.objects.get(pk=pk)
    tags = Tag.objects.all()
    context = {
        'project':project,
        'tags':tags
    }
    return render(request,'single-projects.html',context)