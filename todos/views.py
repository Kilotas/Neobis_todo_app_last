

from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.order_by('-created_at') # get all todos ordered by newest to oldest
    return render(request, 'todos/index.html', {'todos': todos})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = False if not request.POST.get('completed', False) else True
        Todo.objects.create(title=title, description=description, completed=completed)
        return redirect('todos:index')
    else:
        return render(request, 'todos/create.html')

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = False if not request.POST.get('completed', False) else True
        todo.title = title
        todo.description = description
        todo.completed = completed
        todo.save()
        return redirect('todos:index')
    else:
        return render(request, 'todos/update.html', {'todo': todo})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos:index')

