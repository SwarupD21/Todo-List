from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import decorators

# Create your views here.
@login_required
def task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        # print(title)
        Task.objects.create(
            user = request.user,
            title = title,
            description=description
        )
        return redirect('task')
    queryset = Task.objects.filter(user = request.user)
    context = {'tasks':queryset}
    return render(request,'taskform.html',context)

@login_required
def task_update(request,id):
    queryset = Task.objects.get(id=id,user=request.user)
    if request.method=="POST":
        data = request.POST
        title = data.get("title")
        description=data.get("description")

        queryset.title=title
        queryset.description=description
        queryset.save()
        return redirect('task')
    context = {'tasks':queryset}
    return render(request,'update_taskform.html',context)

@login_required
def task_complete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.state = not task.state
    task.save()
    return redirect('task')

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('task')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                    "error": "Username already exists"
                })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("logged_in")
    return render(request, "register.html")

def logged_in(request):
    if request.method=="POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('task')
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect("logged_in")