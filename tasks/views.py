from django.shortcuts import get_object_or_404, redirect, render
from .forms import  TaskForms  # (Dhyan rakhna agar teri forms.py mein TaskForm naam hai)
from .models import Task


def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
  if request.method == 'POST':
    form = TaskForms(request.POST)
    if form.is_valid():  # yahan underscore _ zaroori hai
      form.save()
      return redirect('task_list')  # URL ka naam dena hai, file ka nahi
  else:
    form = TaskForms()

  # Naya form dikhane ke liye task_form.html render hoga
  return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, pk):
  task = get_object_or_404(Task, pk=pk)

  if request.method == 'POST':
    form = TaskForms(request.POST, instance=task)  # POST hamesha capital hoga
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForms(instance=task)

  # Edit form dikhane ke liye bhi task_form.html render hoga
  return render(request, 'tasks/task_form.html', {'form': form})


def task_delete(request,pk):
  task = get_object_or_404(Task,pk=pk)
  task.delete()
  return redirect('task_list')
  
