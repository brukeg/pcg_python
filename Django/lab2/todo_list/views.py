from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import ToDo


# Create your views here.
def index(request):
    # return HttpResponse('ok')  # display form and items
    todo = get_object_or_404(ToDo)
    return render(request, 'todo_list/index.html,', {'todo': todo})


def add_todo(request, pk):  # similar to blog example
    # todo.add()
    # return HttpResponse('success')  # display form and todos
    todo = get_object_or_404(ToDo, pk=pk)
    todo.text = request.POST['text']
    todo.created_date = timezone.now()
    todo.save()
    return render(request, 'todo_list/index.html', {'todo': todo})


def toggle_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.toggle()
    return HttpResponse('success')  # replace with button


def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return HttpResponse('success')  # replace with button


def edit_todo(request, pk):
    # return HttpResponse('success')  # replace with button
    todo = get_object_or_404(ToDo, pk=pk)
    todo.text = request.POST['text']
    todo.created_date = timezone.now()
    todo.save()
    return render(request, 'todo_list/index.html,', {'todo': todo})
