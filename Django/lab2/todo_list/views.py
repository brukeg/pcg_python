from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import ToDo


# Create your views here.
def index(request):
    todos = ToDo.objects.all().order_by('-created_date', 'completed_date')
    return render(request, 'todo_list/index.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        print(request.POST)
        text_from_input = request.POST['todo']  # name in index name='todo'
        todo = ToDo(text=text_from_input)
        todo.save()
    return redirect('todos:index')  # app name from urls.py


def toggle_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.toggle()
    return redirect('todos:index')


def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('todos:index')


def edit_todo(request, pk):
    # return HttpResponse('success')  # replace with button
    todo = get_object_or_404(ToDo, pk=pk)
    todo.text = request.POST['text']
    todo.created_date = timezone.now()
    todo.save()
    return render(request, 'todo_list/index.html', {'todo': todo})
