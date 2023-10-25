from django.shortcuts import render, redirect
from .models import hiitTodo, Comment
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, user_logged_out

@login_required(login_url='/todo/login')
def home(requests):
    todos = hiitTodo.objects.filter(completed = False)
    data = {'todos':todos}
    return render(requests, 'home.html', context= data)

@login_required(login_url='/todo/login')
def completed_todo(requests):
    todos = hiitTodo.objects.filter(completed = True)
    data = {'todos':todos}
    return render(requests, 'completed_todo.html', context= data)

def goodbye(requests):
    return render(requests, 'goodbye.html')

@login_required(login_url='/todo/login')
def createtodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            result = form.save(commit = False)
            result.author = request.user
            result.completed = False
            result.save()
            return redirect('/todo/home')
            
    return render(request, 'createtodo.html', context={'form':form})

def register(request):
    form = UserCreationForm
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/todo/home')
    return render(request, 'auth/register.html', context={'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
         
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/todo/home')
        else:
            return render(request, 'auth/login.html', context={'message':'User does not exist'})
    return render(request, 'auth/login.html')

@login_required(login_url = '/todo/login')
def display_todo(request,pk):
    todo = hiitTodo.objects.get(pk=pk) 
    comments = Comment.objects.filter(todo=todo)
    if request.method =='POST':
        comment = request.POST.get('comment')
        if comment:
            author = request.user
            data = Comment(comment=comment, author=author, todo=todo)
            data.save()
    return render(request, 'displaytodo.html', context= {'todo':todo, 'comments':comments})


@login_required(login_url='/todo/login')
def logout_user(request):
    logout(request)
    return redirect('/todo/login')

@login_required(login_url='/todo/login')
def delete_todo(request, pk):
    hiitTodo.objects.get(pk=pk).delete()
    return redirect('/todo/home')

@login_required(login_url='/todo/login')
def complete_todo(request, pk):
    hiitTodo.objects.filter(pk=pk).update(completed = True)
    return redirect('/todo/home')