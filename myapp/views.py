from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTasks, CreateNewProject
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    title = "Django Course"
    return render(request,'index.html', {
        'title': title
    })

def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


@csrf_exempt
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTasks()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
@csrf_exempt
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
        
def project_detail(request, id):
    projects = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'projects':projects,
        'tasks':tasks
    })
    