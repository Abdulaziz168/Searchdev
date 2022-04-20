from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag,Review
from .forms import ProjectForm




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


def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")
    else:
        form = ProjectForm()

    form = ProjectForm()
    context = {'form':form}
    return render (request,'project_form.html',context)


def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)


    if request.method == "POST":
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    else:
        form = ProjectForm()

    form = ProjectForm()
    context = {'form':form,
            'project':project}
    return render (request,'project_form.html',context)



def delateProject(request,pk):
    project = Project.objects.get(id=pk)
    
    context = {}
    return render (request,'delate_project.html',context)