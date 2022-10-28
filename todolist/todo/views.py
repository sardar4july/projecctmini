from django.shortcuts import render, redirect
from . models import *


def index(request):
    data = Todo.objects.all()
    if request.method == 'POST':
        todo = request.POST['title']
        new_todo = Todo(title=todo)
        new_todo.save()
        return redirect('/')
    return render(request,'index.html',{'todo':data})


def delete(request,pk):
    data = Todo.objects.get(id=pk)
    data.delete()
    return redirect("/")


