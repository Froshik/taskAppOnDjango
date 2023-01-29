from django.shortcuts import render, redirect
from.models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'myapp1/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'myapp1/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка в форме'

    form = TaskForm()
    context={
        'form': form,
        'error': error
    }
    return render(request, 'myapp1/create.html', context)