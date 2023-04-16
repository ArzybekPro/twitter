from django.shortcuts import render, redirect
from apps.posts.models import Post, Comment, Task
from apps.users.models import User
from apps.posts.forms import UpdateForm,TaskForm
from apps.settings.models import Settings
from django.db.models import Q
from .forms import TaskForm


# Create your views here.

def update_post(request, id):
    settings = Settings.objects.latest('id')
    post = Post.objects.get(id=id)
    if request.user == post.user:
        if request.method == 'POST':
            file = request.FILES.get('file')
            text = request.POST.get('text')
            if file:
                try:
                    post.text = text
                    post.image = file
                    post.video = file
                    post.save()

                    return redirect('index')
                except:
                    post.video = file
                    post.image = file
                    post.text = text
                    post.save()
                    return redirect('index')
            else:
                post.video = file
                post.image = file
                post.text = text
                post.save()
                return redirect('index')
    else:
        return redirect('index')

    context = {
        'post': post,
        'settings': settings
    }
    return render(request, 'posts/update_post.html', context)


def post_delete(request, id):
    settings = Settings.objects.latest('id')
    post = Post.objects.get(id=id)
    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
            return redirect('index')

    else:
        return redirect('index')
    return render(request, 'posts/post_delete.html')


def comment_delete(request, id):
    settings = Settings.objects.latest('id')
    comment = Comment.objects.get(id=id)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('index')
    else:
        return redirect('index')
    return render(request, 'posts/comment.html')


def search(request):
    posts = Post.objects.all()
    users = User.objects.all()
    search_key = request.GET.get('key')
    if search_key:
        posts = Post.objects.all().filter(Q(text__icontains=search_key))
        users = User.objects.all().filter(Q(username__icontains=search_key))
    context = {
        'users': users,
        'posts': posts,
    }
    return render(request, 'users/search.html', context)


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'posts/todo_list.html', context)

def edit(request,id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None ,instance =task)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    form = UpdateForm(request.POST or None,instance=task)
    context = {
        'form': form
    }
    return render(request, 'posts/edit.html', context)

def completed(request , id):
    task = Task.objects.get(id=id)
    if task.comleted != True:
        task.save()
        return redirect('home:home')

def delete(request,id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('home:home')

def filter_priority(request,choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    tasks = Task.objects.filter(priority = choice)
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'posts/todo_list.html', context)

def filter_status(request,choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    tasks = Task.objects.filter(status = choice)
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'posts/todo_list.html', context)

