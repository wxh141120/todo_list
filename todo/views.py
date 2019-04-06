from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Todo
from django.template import RequestContext

# Create your views here.
# def todo(request):
#     if request.method == 'POST':
#         if request.POST['thing'] == '':
#             return render(request, 'todo.html')
#         else:
#             todo = Todo(thing=request.POST['thing'], done=False)
#             todo.save()
#             content = {'list': Todo.objects.all()}
#             return render(request, 'todo.html', content)
#             # return render_to_response('todo.html', content)
#     elif request.method == 'GET':
#         content = {'list': Todo.objects.all()}
#         return render(request, 'todo.html', content)

    # return render(request, 'todo.html')
    # return HttpResponse('Todo List!')

def get(request):
    '''获取所有任务清单'''
    todo_list = Todo.objects.all()
    return render(request, 'todo.html', {'todo_list': todo_list})


def add(request):
    if request.method == "GET":
        # return render(request, 'todo.html')
        todo_list = Todo.objects.all()
        return render(request, 'todo.html', {'todo_list': todo_list})
    elif request.method == 'POST':
        thing = request.POST.get('thing')
        Todo.objects.create(thing=thing)
        todo_list = Todo.objects.all()
        return render(request, 'todo.html', {'todo_list': todo_list})
        # return redirect('get')


def delete(request):
    id = request.GET.get('id')
    Todo.objects.filter(id=id).delete()
    todo_list = Todo.objects.all()
    return render(request, 'todo.html', {'todo_list': todo_list})


def edit(request):
    if request.method == 'GET':
        todo_list = Todo.objects.all()
        return render(request, 'todo.html', {'todo_list': todo_list})
    elif request.method == 'POST':
        id = request.POST.get('id')
        thing = request.POST.get('thing')
        Todo.objects.filter(id=id).update(thing=thing)
        todo_list = Todo.objects.all()
        return render(request, 'todo.html', {'todo_list': todo_list})
