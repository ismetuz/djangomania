from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from todo.models import Todo, TodoCategory, TodoTag
# from django.http import HttpResponse, Http404

    # todos = Todo.objects.filter(
    #     is_active=True,
    #     title__icontains ='todo'  #burada title içinde todo olanları da filtreledik
    #     ) 
    # Hem is_active olacak hemde title içinde todo yazacak
    # eğer bir metnin içinde küçük büyük harf duyarlılığı olmadan bir kelime harf arayacaksak title__icontains='todo' 
@login_required(login_url='/admin/login/')
def all_todos_view(request):
    todos = Todo.objects.filter(is_active=True, user= request.user)
    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)

@login_required(login_url='/admin/login/')
def todo_detail_view(request,id,category_slug):
    todo = get_object_or_404(
        Todo,
        category__slug=category_slug, 
        pk=id)
    context = dict(
        todo = todo,
    )
    return render(request,'todo/todo_detail.html', context)

@login_required(login_url='/admin/login/')
def category_view(request, category_slug):
    category = get_object_or_404(TodoCategory, slug=category_slug)
    todos= Todo.objects.filter(
        is_active=True,
        category=category,
        user=request.user,
    )
    context = dict(
        todos=todos,
        category=category,
    )
    return render(request, 'todo/todo_list.html',context)

@login_required(login_url='/admin/login/')
def tag_view(request,tag_slug):
    tag = get_object_or_404(TodoTag, slug=tag_slug)
    context = dict(
        todos=tag.todo_set.filter( user=request.user ),
        tag = tag,
    )
    return render(request, 'todo/todo_list.html', context)