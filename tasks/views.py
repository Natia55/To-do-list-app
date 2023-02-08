from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TasksForm


def list_tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_tasks(request):
    if request.method == 'GET':
        form = TasksForm

        return render(request, 'tasks/create_tasks.html', {'form': form})

    elif request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TasksForm()
    return render(request, 'tasks/create_tasks.html', {'form': form})


def delete_tasks(request, pk):
    tasks = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('list_tasks')
    return render(request, 'tasks/delete_tasks.html', {'tasks': tasks})


def update_tasks(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TasksForm(instance=task)
    return render(request, 'tasks/update_tasks.html', {'form': form})


