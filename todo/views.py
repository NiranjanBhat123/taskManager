from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from .models import Task
from datetime import datetime
from django.utils import timezone



# Create your views here.


def loginn(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"user does not exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"invalid credentials")
    
    return render(request,'login.html')

def signupp(request):
    try:
        if request.method=='POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            print(username,password,email)
            my_user = User.objects.create_user(username,email,password)
            my_user.save()
            if my_user is not None:
                login(request,my_user)
                return redirect('/')
            return redirect('/login')
    except:
        invalid = "User already exists"
        return render(request, 'signup.html', {'invalid': invalid})
    
    return render(request,'signup.html')
        
        
            

@login_required(login_url='login/')
def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        if not date:
            date = None
        user = request.user
        Task.objects.create(
            user = user,
            title = title,
            description= description,
            deadline = date,
            
        )
        return redirect('/')
    return render(request,'home.html',{'user':request.user})


@login_required(login_url='login/')
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    now = datetime.now().date
    context = {'tasks':tasks,'user':request.user,'now':now}
    return render(request,'tasks.html',context)

@login_required(login_url='login/')
def logoutt(request):
    print("logging out ",request.user)
    logout(request)
    return redirect('/')


@login_required(login_url='login/')
def completed(request,message_id):
    task = get_object_or_404(Task,id = message_id)
    print(f"marking {task} as completed")
    if request.method== 'POST':
        print(task,task.completed)
        task.completed = True
        print(task,task.completed)
        task.save()
        return JsonResponse({'success':True})
    return JsonResponse({'sucess':False})


@login_required(login_url='login/')
def delete_message(request, message_id):
    message = get_object_or_404(Task, id=message_id)
    if request.method == 'POST':
        message.delete()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


@login_required(login_url='login/')
def profile(request):
    user = request.user
    total_tasks = Task.objects.filter(user=user).count()
    completed_tasks = Task.objects.filter(user=user,completed=True).count()
    overdue_tasks = Task.objects.filter(user=user, deadline__lt=timezone.now(), completed=False).count()

    pending_tasks = total_tasks - completed_tasks - overdue_tasks
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'pending_tasks': pending_tasks,
    }
    return render(request,'profile.html',context)



    