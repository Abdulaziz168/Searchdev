from django.shortcuts import render
from django.http import HttpResponse


projectsList = [{
    'id':'1',
    'title':'Ecommerce Website',
    'description':'Fully functional ecommerce website'
},
{
    'id':'2',
    'title':'Portfolio Website',
    'description':'This was a project where I build'
},
{
    'id':'3',
    'title':'Social Network',
    'description':'Awesome open source project I am still working on'
},
]


def projects(request):
    return render(request,'projects.html')


def project(request,pk):

    context = {
    }
    return render(request,'single-projects.html',context)